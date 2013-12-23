" cscope-loader.vim

function! CsLoad()
    pyfile csload.py
    python load()
endfunction

function! CsReload()
    pyfile csload.py
    python reload()
endfunction

function! CsHome()
    pyfile csload.py
    python getHome()
endfunction

command! -nargs=0 CsLoad call CsLoad()
command! -nargs=0 CsReload call CsReload()
command! -nargs=0 CsHome call CsHome()
