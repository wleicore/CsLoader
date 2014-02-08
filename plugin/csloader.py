# !/usr/bin/env python
# -*-coding:utf-8-*-
# file csload.py

import os
import shutil
import vim

ROOT = os.getenv("HOME") + "/.cscope-loader/"

FIND_CMD = "find . -name \*.java -o -name \*.h -o -name \*.c -o -name \*.cpp -o -name \*.xml> cscope.files"
CSCOPE_CMD = "cscope -bq"
TAGS_CMD = "ctags --file-scope=no -R `pwd`"

def getHome():
    cwd = os.getcwd()
    home = hash(cwd)
    return ROOT + str(home)

def csDbFile():
    return getHome() + "/cscope.out"

def tagsFile():
    return getHome() + "/tags"

def mkCsDb():
    try:
        os.system(FIND_CMD)
        os.system(CSCOPE_CMD)
        os.system(TAGS_CMD)
        home = getHome()

        # move cscope.* and tags to ~/.cscope-loader/[hash]
        if os.path.exists(home) == False:
            os.makedirs(home)
        os.system("mv cscope.* " + home)
        os.system("mv tags " + home)
    except Exception as e:
        print e

def loadCsAndTags():
    try:
        vim.command("cs add " + csDbFile())
        # 防止cscope的重复链接
        vim.command("cs reset")
        vim.command("set tags=" + tagsFile())
    except Exception as e:
        print e

def load():
    if os.path.exists(csDbFile()):
        loadCsAndTags()
    else:
        mkCsDb()
        loadCsAndTags()
    print "load cscope and tags ok!"

def reload():
    mkCsDb()
    loadCsAndTags()
    print "reload cscope and tags ok!"

def printHome():
    print getHome()

def cleanHome():
    home = getHome()
    if os.path.exists(home):
        print "clean home ok!"
        shutil.rmtree(home)
    else:
        print "Abort, " + home + " is not exists!"

def onInit():
    home = getHome()
    if os.path.exists(home):
        loadCsAndTags()
        print "\'CsLoad\' excuted"
    else:
        print "Excute \'CsLoad\' to connect cscope and tags!"
