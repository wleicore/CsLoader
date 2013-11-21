" Load ctags
function! LoadTags()
    if has("ctags")
        set tags=tags
        set autochdir
    endif
endfunction

" Load cscope 
function! LoadCscope()
    set csto=1
    set cst
    set nocsverb
    if filereadable("cscope.out")
        cs add cscope.out
    endif
    set csverb
endfunction

function! CreateCscopeDb()
    call system("find . -name \*.java -o -name \*.h -o -name \*.c -o -name \*.cpp -o -name \*.xml> cscope.files")
    call system("cscope -bq")
    call LoadCscope()
endfunction

function! CreateTags()
    call system("ctags -R")
    call LoadTags()
endfunction

function! LoadCscopeProject()
    if filereadable("cscope.out")
        call LoadCscope()
    else
        echo "cscope.out not found, create it..."
        call CreateCscopeDb()
    endif
    if filereadable("tags")
        call LoadTags()
    else
        echo "tags not found, create it..."
        call CreateTags()
    endif
    echo "Load cscope project success!"
endfunction

function! ReloadCscopeProject()
    echo "Reload cscope db"
    call CreateCscopeDb()
    echo "Reload tags"
    call CreateTags()
    echo "Reload success!"
endfunction

command CsLoad call LoadCscopeProject()
command CsReload call ReloadCscopeProject()
