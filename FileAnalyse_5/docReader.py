import os
import re
import shutil


# 产品类1:文本文件读取类
class txtReader:

    __rootPath = ''
    # 单个文件最终地址(加标题)
    __addressPath = ''

    __fileName = []

    def setRootPathFunc(self, RootPath):
        self.__rootPath = RootPath

    def setAddressPathFunc(self, FilePath):
        self.__addressPath = FilePath

    def setFileNameFunc(self):
        for fileName in os.listdir(self.__rootPath):
            if len(re.findall(r'\.txt$', fileName)):  # bu ke xin
                self.__fileName.append(fileName)

    def getRootPathFunc(self):
        return self.__rootPath

    def getAddressPathFunc(self):
        return self.__addressPath

    def getFileNameFunc(self):
        self.setFileNameFunc()
        return self.__fileName

    def _openFileFunc(self, filename):
        return _openFileFunc(os.path.join(self.__rootPath, filename))

    def mkFile(self, title, packge='', root='E:\\python\\FileAnalyse\\裁判文书样本'):
        mkFile(root, packge, title)




# 产品类2:hadoop路径文件读取类
class hadoopReader:

    __rootPath = 'hadoop路径'
    # 单个文件最终地址(加标题)
    __addressPath = ''

    __fileName = []

    def setRootPathFunc(self, RootPath):
        self.__rootPath = RootPath

    def setAddressPathFunc(self, FilePath):
        self.__addressPath = FilePath

    def getRootPathFunc(self):
        return self.__rootPath

    def getAddressPathFunc(self):
        return self.__addressPath

    def getFileNameFunc(self):
        return self.__fileName

    def _openFileFunc(self):
        pass
        # 调用能打开hadoop文件的方法

    def getFileNameFunc(self):
        for fileName in os.listdir(self.__rootPath):
            self.__fileName.append(fileName)

def _openFileFunc(addressPath):
    if os.path.isfile(addressPath):
        return open(addressPath, encoding='UTF-8').read()
    else:
        return


def mkFile(rootPath, packge, Title):
    if packge != '':
        path = os.path.join(rootPath, packge)
        if not os.path.isdir(path):
            try:
                os.makedirs(path)
            except NotADirectoryError:
                print("创建" + packge + "文件夹出错")
        filePath = os.path.join(path, Title)
        if not os.path.isfile(filePath):
            try:
                shutil.copy(os.path.join(rootPath, Title), filePath)
            except OSError:
                print("错误文件复制失败")