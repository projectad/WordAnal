# -*- coding: utf-8 -*-
import docWRer

def main():
    filetype = docWRer.fileReader()
    docreader = filetype.get_localizer('txt')
    docreader.setRootPathFunc('E:\\python\\FileAnalyse\\裁判文书样本')
    docreader.docDealFunc()

main()


