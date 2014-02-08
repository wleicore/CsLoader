" cscope-loader.vim

let s:plugin_path = escape(expand('<sfile>:p:h'), '\')
if !exists('s:python_loaded')
    exe 'pyfile ' . fnameescape(s:plugin_path) . '/csloader.py'
    let s:python_loaded=1
endif

function! CsLoad()
    python load()
endfunction

function! CsReload()
    python reload()
endfunction

function! CsHome()
    python printHome()
endfunction

function! CsClean()
    python cleanHome()
endfunction

command! -nargs=0 CsLoad call CsLoad()
command! -nargs=0 CsReload call CsReload()
command! -nargs=0 CsHome call CsHome()
command! -nargs=0 CsClean call CsClean()

python onInit()
