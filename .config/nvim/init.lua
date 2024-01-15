-- Use the Pathogen plugin manager.
vim.cmd([[execute pathogen#infect()]])

vim.cmd([[map D /^\(.*\)\n\ze\%(.*\n\)*\1$<cr>]])

-- Use system clipboard.
vim.cmd([[set clipboard=unnamedplus]])

-- Set the colorscheme.
vim.opt.syntax = "on"
vim.opt.background = "dark"
vim.cmd([[
let ayucolor="dark"
colorscheme ayu
highlight Comment cterm=italic gui=italic
]])
vim.g.airline_theme = "ayu_dark"

-- Set the cursor style.
vim.opt.termguicolors = true
vim.cmd([[highlight Cursor gui=reverse guifg=NONE guibg=NONE]])

-- Enable Ruff LSP.
require('lspconfig').ruff_lsp.setup {
  on_attach = on_attach,
  init_options = {
    settings = {
      args = {},
    }
  }
}

-- Set leader and localleader.
vim.cmd([[
:let mapleader = ","
:let maplocalleader = ";"
]])

-- " Configure the user interface.
vim.cmd([[
filetype plugin indent on
set number
set wildmenu
set cursorline
set ruler
set lazyredraw
set signcolumn=yes:1
]])

-- Insert whitespace in normal mode.
vim.cmd([[
nnoremap <Space> i<Space><Right><ESC>
nnoremap <Tab> i<Tab><Right><ESC>
nnoremap <CR> i<CR><Right><ESC>
]])

-- Set default width.
vim.cmd([[
set colorcolumn=80,100,120
]])

-- Show matching parenthesis.
vim.cmd([[
set showmatch
]])

-- Search while typing and highlight results.
vim.cmd([[
set incsearch
set hlsearch
]])

-- Use four spaces for tabs.
vim.cmd([[
set tabstop=4
set shiftwidth=4
set expandtab
autocmd FileType yaml setlocal ts=2 sts=2 sw=2 expandtab
autocmd FileType json setlocal ts=2 sts=2 sw=2 expandtab
autocmd FileType javascript setlocal ts=2 sts=2 sw=2 expandtab
autocmd FileType html setlocal ts=2 sts=2 sw=2 expandtab
autocmd FileType css setlocal ts=2 sts=2 sw=2 expandtab
autocmd FileType typescript setlocal ts=2 sts=2 sw=2 expandtab
autocmd FileType r setlocal ts=2 sts=2 sw=2 expandtab
autocmd FileType markdown setlocal ts=2 sts=2 sw=2 expandtab
autocmd FileType lua setlocal ts=2 sts=2 sw=2 expandtab
autocmd FileType tex setlocal ts=2 sts=2 sw=2 expandtab
autocmd FileType svg setlocal ts=2 sts=2 sw=2 expandtab
autocmd FileType caddyfile setlocal ts=4 sts=4 sw=4 noexpandtab
]])

-- Move fast in a line.
vim.cmd([[
nnoremap j gj
nnoremap k gk
nnoremap B ^
nnoremap E $
]])

-- Move fast in a file.
vim.cmd([[
map J )
map K (
]])

-- Toggle the NERDTree with 'Ctrl' + 'n'.
vim.cmd([[
nnoremap <C-n> :NERDTreeToggle<CR>
]])

-- Stop highlighting of search results with 'no'.
vim.cmd([[
nnoremap no :nohlsearch<CR>
]])

-- Check spelling for English and German.
vim.cmd([[
set spell spelllang=en,de
]])

-- Move to miss-spelled words with 'zn' / 'zN'.
vim.cmd([[
nnoremap zn ]s
nnoremap zN [s
]])

-- Remove trailing whitespace with ':NoTWS'.
vim.cmd([[
:command NoTWS :%s/\s\+$/
:command NoWS :%s/^  $/
]])

-- Remove NeoVim swap files with ':NoSwap'.
vim.cmd([[
:command NoSwap :! rm -rf $HOME/.local/state/nvim/swap/*%.swp
]])

-- Only allow certain plugins.
vim.cmd([[
:let g:airline_extensions = []
]])

-- Motion in CamelCase.
vim.cmd([[
map <silent> w <Plug>CamelCaseMotion_w
map <silent> b <Plug>CamelCaseMotion_b
map <silent> e <Plug>CamelCaseMotion_e
map <silent> ge <Plug>CamelCaseMotion_ge
sunmap w
sunmap b
sunmap e
sunmap ge
]])

-- Create number sequence.
vim.cmd([[map # g<C-a>]])

-- Docstrings
vim.cmd([[
let g:doge_doc_standard_python = 'google'
]])

-- Lilypond
vim.cmd([[
filetype off
set runtimepath+=/usr/share/lilypond/2.24.1/vim/
filetype on
]])

vim.cmd([[
" Format Python code with ':Black'.
:command Black :w | ! black %
" Sort Python imports with ':ISort'.
:command ISort :w | ! isort --profile black %
" Lint Python code with ':Pylint'.
:command Pylint :w | ! pylint %
" Test Python code with ':Pytest'.
:command Pytest :w | ! pytest %
" Format Python code with ':Ruff'.
:command Ruff :w | ! ruff --fix format %
" Format R code with ':Styler'.
:command Styler :w | ! Rscript -e "styler::style_file('%')"
" Format Go code with ':GoFmt'.
:command GoFmt :w | ! gofmt -s -w %
" Format JavaScript and TypeScript code with ':Prettier'.
:command Prettier :w | ! prettier --write %
" Format code with ':Biome'.
:command Biome :w | ! biome format --write %
" Save and commit.
:command C :w | ! git update %
" Save and run.
:command Ly :w | ! lilypond %
]])

-- VimDevIcons
vim.cmd([[
let g:webdevicons_conceal_nerdtree_brackets=1
]])

-- coc.nvim
vim.cmd([[
inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"
]])

-- Set font.
vim.cmd([[
set guifont=ComicCode\ Nerd\ Font

filetype off
set runtimepath+=/usr/share/lilypond/2.22.1/vim/
filetype on

" Define comments for lilypond
autocmd FileType lilypond setlocal commentstring=%\ %s
]])

