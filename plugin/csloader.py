# !/usr/bin/env python
# -*-coding:utf-8-*-
# file csload.py

import os
import shutil
import vim

__ROOT = os.getenv("HOME") + "/.cscope-loader/"

__FIND_CMD = "find . -name \*.java -o -name \*.h -o -name \*.c -o -name \*.cpp -o -name \*.xml> cscope.files"
__CSCOPE_CMD = "cscope -bkq -i cscope.files"
__TAGS_CMD = "ctags --file-scope=no -R `pwd`"

def __getHome():
    cwd = os.getcwd()
    home = hash(cwd)
    return __ROOT + str(home)

def __csDbFile():
    return __getHome() + "/cscope.out"

def __tagsFile():
    return __getHome() + "/tags"

def __mkCsDb():
    try:
        os.system(__FIND_CMD)
        os.system(__CSCOPE_CMD)
        os.system(__TAGS_CMD)
        home = __getHome()

        # move cscope.* and tags to ~/.cscope-loader/[hash]
        if os.path.exists(home) == False:
            os.makedirs(home)
        os.system("mv cscope.* " + home)
        os.system("mv tags " + home)
    except Exception as e:
        print e

def __loadCsAndTags():
    try:
        vim.command("cs add " + __csDbFile())
        # 防止cscope的重复链接
        vim.command("cs reset")
        vim.command("set tags=" + __tagsFile())
    except Exception as e:
        print e

def load():
    if os.path.exists(__csDbFile()):
        __loadCsAndTags()
    else:
        __mkCsDb()
        __loadCsAndTags()
    print "load cscope and tags ok!"

def reload():
    __mkCsDb()
    __loadCsAndTags()
    print "reload cscope and tags ok!"

def printHome():
    print __getHome()

def cleanHome():
    home = __getHome()
    if os.path.exists(home):
        print "clean home ok!"
        shutil.rmtree(home)
    else:
        print "Abort, " + home + " is not exists!"

def loadWhenStart():
    home = __getHome()
    if os.path.exists(home):
        __loadCsAndTags()
