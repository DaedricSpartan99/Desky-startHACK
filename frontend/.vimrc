call plug#begin()
" The default plugin directory will be as follows:
"   - Vim (Linux/macOS): '~/.vim/plugged'
"   - Vim (Windows): '~/vimfiles/plugged'
"   - Neovim (Linux/macOS/Windows): stdpath('data') . '/plugged'
" You can specify a custom plugin directory by passing it as the argument
"   - e.g. `call plug#begin('~/.vim/plugged')`
"   - Avoid using standard Vim directory names like 'plugin'

Plug 'mxw/vim-jsx'
Plug 'pangloss/vim-javascript'

Plug 'SirVer/ultisnips'
Plug 'mlaursen/vim-react-snippets'

Plug 'vim-airline/vim-airline'

Plug 'preservim/nerdtree'
Plug 'sainnhe/sonokai'

" Initialize plugin system
" - Automatically executes `filetype plugin indent on` and `syntax enable`.
call plug#end()

let g:jsx_ext_required = 0 
syntax on
set number

" NERDTree environment 
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>

autocmd VimEnter * NERDTree | wincmd p

colorscheme sonokai

" Indent
" set expandtab
" set tabstop=2
" set shiftwidth=2
