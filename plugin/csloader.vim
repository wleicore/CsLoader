" cscope-loader.vim

let s:plugin_path = escape(expand('<sfile>:p:h'), '\')
if !exists('s:python_loaded')
    exe 'pyfile ' . fnameescape(s:plugin_path) . '/csloader.py'
    let s:python_loaded=1
endif

func! CsLoad()
    python load()
endf

func! CsReload()
    python reload()
endf

func! CsHome()
    python printHome()
endf

func! CsClean()
    python cleanHome()
endf

command! -nargs=0 CsLoad call CsLoad()
command! -nargs=0 CsReload call CsReload()
command! -nargs=0 CsHome call CsHome()
command! -nargs=0 CsClean call CsClean()

if exists('g:csloader_auto_load_when_exists')
    python init()
endif
