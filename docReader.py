import os


# 工厂类
class fileReader:
    def get_localizer(self, fileType = "txt"):
        FileType = dict(txt=txtReader, hadoop=hadoopReader)
        return FileType[fileType]()

# 产品类1:文本文件读取类
class txtReader:

    __rootPath = 'E:\\python\\FileAnalyse\\裁判文书样本'
    # 单个文件最终地址(加标题)
    __addressPath = ''

    def setRootPathFunc(self, RootPath):
        self.__rootPath = RootPath

    def getRootPathFunc(self):
        return self.__rootPath

    def setAddressPathFunc(self, FilePath):
        self.__addressPath = FilePath

    def getAddressPathFunc(self):
        return self.__addressPath

    def openFileFunc(self):
        return openFileFunc(self.__addressPath)
# 产品类2:hadoop路径文件读取类
class hadoopReader:

    __rootPath = 'hadoop路径'
    # 单个文件最终地址(加标题)
    __addressPath = ''

    def setRootPathFunc(self, RootPath):
        self.__rootPath = RootPath

    def getRootPathFunc(self):
        return self.__rootPath

    def setAddressPathFunc(self, FilePath):
        self.__addressPath = FilePath

    def getAddressPathFunc(self):
        return self.__addressPath

    def openFileFunc(self):
        pass
        # 调用能打开hadoop文件的方法

def openFileFunc(addressPath):
    if os.path.isfile(addressPath):
        return open(addressPath, encoding='UTF-8').read()
    else:
        return