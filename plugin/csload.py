# file csload.py

import os
import vim

ROOT = os.getenv("HOME") + "/.cscope-loader/"

FIND_CMD = "find . -name \*.java -o -name \*.h -o -name \*.c -o -name \*.cpp -o -name \*.xml> cscope.files"
CSCOPE_CMD = "cscope -bq"
TAGS_CMD = "ctags -R"

def getHome():
    cwd = os.getcwd()
    home = hash(cwd)
    return ROOT + str(home)

def csDbFile():
    return getHome() + "/cscope.out"

def tagsFile():
    return getHome() + "/tags"

def mkCsDb():
    os.system(FIND_CMD)
    os.system(CSCOPE_CMD)
    os.system(TAGS_CMD)
    home = getHome()

    # move cscope.* and tags to ~/.cscope-loader/[hash]
    os.makedirs(home)
    os.system("mv cscope.* " + home)
    os.system("mv tags " + home)

def loadCsAndTags():
    vim.command("cs add " + csDbFile())
    vim.command("set tags=" + tagsFile())

def load():
    if os.path.exists(csDbFile()):
        loadCsAndTags()
    else:
        mkCsDb()
        loadCsAndTags()

def reload():
    mkCsDb()
    loadCsAndTags()
