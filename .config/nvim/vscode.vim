
" --- HORIZONTAL RULER ---

set colorcolumn=80


" --- MOUSE SCROLLING ---

set mouse=a


" --- COPY TO CLIPBOARD ---

set clipboard=unnamedplus


" --- INSERT WHITESPACE ---

map <CR> i<CR><esc>
map <space> i<space><esc>l
map <tab> i<tab><esc>l


" --- COPY AND REDO ---

map c y
map r <C-r>


" --- ENCODING ---

set encoding=utf-8


" --- SPACES AND TABS ---

set textwidth=79
set shiftwidth=4
set tabstop=4
set softtabstop=4
set expandtab
set shiftround
set autoindent


" --- NO UNNECESSARY REDRAWS ---

set lazyredraw


" --- SHOE PARENTHESIS ---

set showmatch
hi MatchParen cterm=underline ctermbg=none ctermfg=none


" --- MOVEMENT ---

map <up> gk
map <down> gj
map <C-left> ^
map <C-right> $

nnoremap j gj
nnoremap k gk

map g gg

map J jjjjjjj
map K kkkkkkk

map <A-J> )
map <A-K> (


" --- TAB AUTOCOMPLETE ---

inoremap <S-tab> <C-x><C-P>
inoremap <C-tab> <C-x><C-P>


" --- CODE FOLDING ---

set foldmethod=indent foldignore=# foldignore=/ foldignore="
set foldnestmax=10
set nofoldenable
set foldlevel=10
nnoremap z za
