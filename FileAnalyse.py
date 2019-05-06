# -*- coding: utf-8 -*-
import os
import docReader
import docWriter


def main():
    filetype = docReader.fileReader()
    docreader = filetype.get_localizer("txt")
    docwriter = docWriter.docWriter()

    for childPath in os.listdir(docreader.getRootPathFunc()):
        docreader.setAddressPathFunc(os.path.join(docreader.getRootPathFunc(), childPath))
        docwriter.setTitle(childPath)
        if docreader.openFileFunc():
            if len(docreader.openFileFunc()) > 200:
                docwriter.setFileContent(docreader.openFileFunc())
                docwriter.docDeal()
                docwriter.dataDeal()
            else:
                os.remove(os.path.join(docreader.getRootPathFunc(), childPath))

main()



