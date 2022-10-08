'use strict'
import { Neovim } from '@chemzqm/neovim'
import { CallHierarchyIncomingCall, CallHierarchyItem, CallHierarchyOutgoingCall, CancellationToken, CancellationTokenSource, Disposable, Position, Range } from 'vscode-languageserver-protocol'
import { TextDocument } from 'vscode-languageserver-textdocument'
import commands from '../commands'
import events from '../events'
import languages from '../languages'
import { TreeDataProvider } from '../tree/index'
import LocationsDataProvider from '../tree/LocationsDataProvider'
import BasicTreeView from '../tree/TreeView'
import { HandlerDelegate, IConfigurationChangeEvent } from '../types'
import { disposeAll } from '../util'
import { isFalsyOrEmpty } from '../util/array'
import { omit } from '../util/lodash'
import window from '../window'
import workspace from '../workspace'
const logger = require('../util/logger')('Handler-callHierarchy')

interface CallHierarchyDataItem extends CallHierarchyItem {
  ranges?: Range[]
  sourceUri?: string
  children?: CallHierarchyItem[]
}

interface CallHierarchyConfig {
  splitCommand: string
  openCommand: string
  enableTooltip: boolean
}

interface CallHierarchyProvider extends TreeDataProvider<CallHierarchyDataItem> {
  meta: 'incoming' | 'outgoing'
  dispose: () => void
}

function isCallHierarchyItem(item: any): item is CallHierarchyItem {
  if (item && typeof item.name === 'string' && item.kind && Range.is(item.range)) return true
  return false
}

export default class CallHierarchyHandler {
  private config: CallHierarchyConfig
  private disposables: Disposable[] = []
  public static commandId = 'callHierarchy.reveal'
  public static rangesHighlight = 'CocSelectedRange'
  private highlightWinids: Set<number> = new Set()
  constructor(private nvim: Neovim, private handler: HandlerDelegate) {
    this.loadConfiguration()
    workspace.onDidChangeConfiguration(this.loadConfiguration, this, this.disposables)
    this.disposables.push(commands.registerCommand(CallHierarchyHandler.commandId, async (winid: number, item: CallHierarchyDataItem, openCommand?: string) => {
      let { nvim } = this
      await nvim.call('win_gotoid', [winid])
      await workspace.jumpTo(item.uri, item.selectionRange.start, openCommand)
      let win = await nvim.window
      win.clearMatchGroup(CallHierarchyHandler.rangesHighlight)
      win.highlightRanges(CallHierarchyHandler.rangesHighlight, [item.selectionRange], 10, true)

      if (!item.ranges?.length) return
      if (item.sourceUri) {
        let doc = workspace.getDocument(item.sourceUri)
        if (!doc) return
        let winid = await nvim.call('coc#compat#buf_win_id', [doc.bufnr])
        if (winid == -1) return
        if (winid != win.id) {
          win = nvim.createWindow(winid)
          win.clearMatchGroup(CallHierarchyHandler.rangesHighlight)
        }
      }
      win.highlightRanges(CallHierarchyHandler.rangesHighlight, item.ranges, 100, true)
      this.highlightWinids.add(win.id)
    }, null, true))
    events.on('BufWinEnter', (_, winid) => {
      if (this.highlightWinids.has(winid)) {
        this.highlightWinids.delete(winid)
        let win = nvim.createWindow(winid)
        win.clearMatchGroup(CallHierarchyHandler.rangesHighlight)
      }
    }, null, this.disposables)
  }

  private loadConfiguration(e?: IConfigurationChangeEvent): void {
    if (!e || e.affectsConfiguration('callHierarchy')) {
      let c = workspace.getConfiguration('callHierarchy', null)
      this.config = {
        splitCommand: c.get<string>('splitCommand'),
        openCommand: c.get<string>('openCommand'),
        enableTooltip: c.get<boolean>('enableTooltip')
      }
    }
  }

  private createProvider(rootItems: CallHierarchyDataItem[], doc: TextDocument, winid: number, kind: 'incoming' | 'outgoing'): CallHierarchyProvider {
    let provider = new LocationsDataProvider<CallHierarchyDataItem, 'incoming' | 'outgoing'>(
      kind,
      winid,
      this.config,
      CallHierarchyHandler.commandId,
      rootItems,
      kind => this.handler.getIcon(kind),
      (el, meta, token) => this.getChildren(doc, el, meta, token)
    )
    for (let kind of ['incoming', 'outgoing']) {
      provider.addAction(`Show ${kind[0].toUpperCase()}${kind.slice(1)} Calls`, (el: CallHierarchyDataItem) => {
        provider.meta = kind as 'incoming' | 'outgoing'
        let rootItems = [omit(el, ['children', 'parent', 'ranges', 'sourceUri'])]
        provider.reset(rootItems)
      })
    }
    return provider
  }

  private async getChildren(doc: TextDocument, item: CallHierarchyItem, kind: 'incoming' | 'outgoing', token: CancellationToken): Promise<CallHierarchyDataItem[]> {
    let items: CallHierarchyDataItem[] = []
    if (kind == 'incoming') {
      let res = await languages.provideIncomingCalls(doc, item, token)
      if (res) items = res.map(o => Object.assign(o.from, { ranges: o.fromRanges }))
    } else {
      let res = await languages.provideOutgoingCalls(doc, item, token)
      if (res) items = res.map(o => Object.assign(o.to, { ranges: o.fromRanges, sourceUri: item.uri }))
    }
    return items
  }

  private async prepare(doc: TextDocument, position: Position, token: CancellationToken): Promise<CallHierarchyItem[] | undefined> {
    this.handler.checkProvier('callHierarchy', doc)
    const res = await languages.prepareCallHierarchy(doc, position, token)
    return isCallHierarchyItem(res) ? [res] : res
  }

  private async getCallHierarchyItems(item: CallHierarchyItem | undefined, kind: 'outgoing'): Promise<CallHierarchyOutgoingCall[]>
  private async getCallHierarchyItems(item: CallHierarchyItem | undefined, kind: 'incoming'): Promise<CallHierarchyIncomingCall[]>
  private async getCallHierarchyItems(item: CallHierarchyItem | undefined, kind: 'incoming' | 'outgoing'): Promise<any> {
    const { doc, position } = await this.handler.getCurrentState()
    const source = new CancellationTokenSource()
    if (!item) {
      await doc.synchronize()
      let res = await this.prepare(doc.textDocument, position, source.token)
      item = res ? res[0] : undefined
      if (!res) throw new Error('Unable to getCallHierarchyItem at current position')
    }
    let method = kind == 'incoming' ? 'provideIncomingCalls' : 'provideOutgoingCalls'
    return await languages[method](doc.textDocument, item, source.token)
  }

  public async getIncoming(item?: CallHierarchyItem): Promise<CallHierarchyIncomingCall[] | undefined> {
    return await this.getCallHierarchyItems(item, 'incoming')
  }

  public async getOutgoing(item?: CallHierarchyItem): Promise<CallHierarchyOutgoingCall[] | undefined> {
    return await this.getCallHierarchyItems(item, 'outgoing')
  }

  public async showCallHierarchyTree(kind: 'incoming' | 'outgoing'): Promise<void> {
    const { doc, position, winid } = await this.handler.getCurrentState()
    await doc.synchronize()
    if (!languages.hasProvider('callHierarchy', doc.textDocument)) {
      void window.showErrorMessage(`CallHierarchy provider not found for current document, it's not supported by your languageserver`)
      return
    }
    const res = await languages.prepareCallHierarchy(doc.textDocument, position, CancellationToken.None)
    const rootItems: CallHierarchyItem[] = isCallHierarchyItem(res) ? [res] : res
    if (isFalsyOrEmpty(rootItems)) {
      void window.showWarningMessage('Unable to get CallHierarchyItem at cursor position.')
      return
    }
    let provider = this.createProvider(rootItems, doc.textDocument, winid, kind)
    let treeView = new BasicTreeView('calls', { treeDataProvider: provider })
    treeView.title = getTitle(kind)
    provider.onDidChangeTreeData(e => {
      if (!e) treeView.title = getTitle(provider.meta)
    })
    treeView.onDidChangeVisibility(e => {
      if (!e.visible) provider.dispose()
    })
    this.disposables.push(treeView)
    await treeView.show(this.config.splitCommand)
  }

  public dispose(): void {
    this.highlightWinids.clear()
    disposeAll(this.disposables)
  }
}

function getTitle(kind: string): string {
  return `${kind.toUpperCase()} CALLS`
}