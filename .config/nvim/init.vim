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
set colorcolumn=80,100,120
" set textwidth=99

" Show matching parenthesis.
set showmatch

" Search while typing and highlight results.
set incsearch
set hlsearch

" Set the colorscheme.
syntax on
set termguicolors
set background=dark
let ayucolor="dark"
colorscheme ayu
highlight Comment cterm=italic gui=italic
let g:airline_theme='ayu_dark'

" Use four spaces for tabs.
set tabstop=4
set shiftwidth=4
set expandtab
autocmd FileType yaml setlocal ts=2 sts=2 sw=2 expandtab
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
set spell spelllang=en,de

" Move to miss-spelled words with 'zn' / 'zN'.
nnoremap zn ]s
nnoremap zN [s

" Remove trailing whitespace with ':NoTWS'.
:command NoTWS :%s/\s\+$/
:command NoWS :%s/^  $/

" Remove NeoVim swap files with ':NoSwap'.
:command NoSwap :! rm -rf $HOME/.local/share/nvim/swap/*.swp

" Only allow certain plugins.
:let g:airline_extensions = []

map <silent> w <Plug>CamelCaseMotion_w
map <silent> b <Plug>CamelCaseMotion_b
map <silent> e <Plug>CamelCaseMotion_e
map <silent> ge <Plug>CamelCaseMotion_ge
sunmap w
sunmap b
sunmap e
sunmap ge

" Docstrings
let g:doge_doc_standard_python = 'google'

" Lilypond
filetype off
set runtimepath+=/home/david/lilypond/usr/share/lilypond/current/vim/
filetype on
syntax on

" Format Python code with ':Black'.
:command Black :! black %

" Sort Python imports with ':ISort'.
:command ISort :! isort --profile black %

" Lint Python code with ':Pylint'.
:command Pylint :w | ! pylint %

" Test Python code with ':Pytest'.
:command Pytest :w | ! pytest %

" Format R code with ':Styler'.
:command Styler :w | ! Rscript -e "styler::style_file('%')"

" Format Go code with ':GoFmt'.
:command GoFmt :w | ! gofmt -s -w %

" Format JavaScript and TypeScript code with ':Prettier'.
:command Prettier :w | ! prettier --write %

" Save and commit.
:command C :w | ! git update %

" Save and run.
:command Ly :w | ! lilypond %

" VimDevIcons
let g:webdevicons_conceal_nerdtree_brackets=1

" coc.nvim
inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"

set guifont=ComicCode\ Nerd\ Font

filetype off
set runtimepath+=/usr/share/lilypond/2.22.1/vim/
filetype on

" Define comments for lilypond
autocmd FileType lilypond setlocal commentstring=%\ %s

" Save a macro for adding two space at the end of the line in register a.
let @a = 'A  j^'
