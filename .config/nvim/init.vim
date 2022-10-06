" Use the Pathogen plugin manager.
execute pathogen#infect()

" Set leader and localleader.
:let mapleader = ","
:let maplocalleader = ";"

" Copy into system clipboard.
set clipboard=unnamedplus

" Configure the user interface.
filetype plugin indent on
set number
set wildmenu
set cursorline
set ruler
set lazyredraw

" Insert whitespace in normal mode.
nnoremap <Space> i<Space><Right><ESC>
nnoremap <Tab> i<Tab><Right><ESC>
nnoremap <CR> i<CR><Right><ESC>

" Highlight search results while typing.
set is hls

" Set default width.
set colorcolumn=100
" set textwidth=99

" Show matching parenthesis.
set showmatch

" Search while typing and highlight results.
set incsearch
set hlsearch

" Use the Solarized colorscheme.
syntax on
set background=dark
" colorscheme nord
colorscheme Atelier_ForestDark
let g:solarized_termcolors=256
set termguicolors
let g:airline_theme='base16_atelier_forest'
" let &t_8f = "\<Esc>[38:2:%lu:%lu:%lum"
" let &t_8b = "\<Esc>[48:2:%lu:%lu:%lum"

" Use four spaces for tabs.
set tabstop=4
set shiftwidth=4
set expandtab
" autocmd FileType yaml setlocal ts=2 sts=2 sw=2 expandtab

" Move fast in a line.
nnoremap j gj
nnoremap k gk
nnoremap B ^
nnoremap E $

" Move fast in a file.
map J jjjjjjj
map K kkkkkkk
map H (
map L )

" Toggle the NERDTree with 'Ctrl' + 'n'.
nnoremap <C-n> :NERDTreeToggle<CR>

" Stop highlighting of search results with 'no'.
nnoremap no :nohlsearch<CR>

" Check spelling for English and German.
set spelllang=en,de

" Move to miss-spelled words with 'zn' / 'zN'.
nnoremap zn ]s
nnoremap zN [s

" Remove trailing whitespace with ':NoTWS'.
:command NoTWS :%s/\s\+$/

" Remove NeoVim swap files with ':NoSwap'.
:command NoSwap :! rm -rf $HOME/.local/share/nvim/swap/*.swp

" Only allow certain plugins.
:let g:airline_extensions = []

" IDEA: Checkout the CtrlP plugin.

map <silent> w <Plug>CamelCaseMotion_w
map <silent> b <Plug>CamelCaseMotion_b
map <silent> e <Plug>CamelCaseMotion_e
map <silent> ge <Plug>CamelCaseMotion_ge
sunmap w
sunmap b
sunmap e
sunmap ge

" Set yaml file indentation to 2 spaces
autocmd FileType yaml setlocal ts=2 sts=2 sw=2 expandtab

" Docstrings
let g:doge_doc_standard_python = 'google'

" Lilypond
filetype off
set runtimepath+=/home/david/lilypond/usr/share/lilypond/current/vim/
filetype on
syntax on

" Format Python code with ':Black'.
:command Black :! black %

" Lint Python code with ':Pylint'.
:command Pylint :! pylint %

" Test Python code with ':Pytest'.
:command Pytest :! pytest %

" Format R code with ':Styler'.
:command Styler :! Rscript -e "styler::style_file('%')"

" Format Go code with ':GoFmt'.
:command GoFmt :! gofmt -s -w %

" " Prettier Settings
" let g:prettier#quickfix_enabled = 0
" let g:prettier#autoformat_require_pragma = 0
" au BufWritePre *.css,*.svelte,*.pcss,*.html,*.ts,*.js,*.json PrettierAsync

" Remove trailing whitespace on save.
" autocmd BufWritePre * :%s/\s\+$//e

" VimDevIcons
let g:webdevicons_conceal_nerdtree_brackets=1

" coc.nvim
inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"
