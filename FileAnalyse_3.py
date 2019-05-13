import os
import shutil
import re
'''class test:
    __rootPath = 'E:\\python\\FileAnalyse\\'
    __getFileParameter = ['DealChongQing', 4, __rootPath, "重庆", 1,"hh"]
    def setFileParameter(self,functionName,parameterNum):
        i = 0
        self.__getFileParameter[0] = functionName
        self.__getFileParameter[1] = parameterNum
        while i < parameterNum:
            self.__getFileParameter[i + 2] = input("输入第{}个参数".format(i+1))
            i = i + 1
    def getFileNameFunc(self):
        sentence = ''
        sentence = sentence + self.__getFileParameter[0] + '('
        i = 1
        while i <= self.__getFileParameter[1]:
            if i != 1:
                sentence = sentence + ','
            if isinstance(self.__getFileParameter[i + 1], str):
                temporaryStr = self.__getFileParameter[i + 1]
                temporaryStr = temporaryStr.replace('\\', "\\\\")
                sentence = sentence + '"' + temporaryStr + '"'
            else:
                sentence = sentence + str(self.__getFileParameter[i + 1])
            i = i+1
        sentence = sentence + ")"
        print(sentence)
    def a(self,test):
        test('E:\\python\\FileAnalyse\\','重庆')
        '''
class docReader:
    __rootPath = 'E:\\python\\FileAnalyse\\裁判文书样本'
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

    '''def movFileFunc(self):
        openFileFunc(self.__addressPath)'''

class docWriter:
    __filecontent = ''
    __Title = ''
    __res0 = []
    __res1 = []
    __res2 = []
    __res3 = []
    __res4 = []
    __res5 = []
    __res6 = []
    __res7 = []
    def mkFile(self,packge = ''):
        mkFile('E:\\python\\FileAnalyse\\裁判文书样本', packge, self.__Title)

    def setFileContent(self, FileContent):
        self.__filecontent = FileContent


    def setTitle(self, Title):
        self.__Title = Title

    def docDeal(self):
        self.__res0 = self.selectNumofInstance()
        self.__res1 = self.selectCity()
        self.__res2 = self.selectFileType()
        self.__res3 = self.selectTime()
        self.__res4 = self.selectJudgmentResult()
        self.__res5 = self.selectDefendant()
        self.__res6 = self.selectRequest()
        self.__res7 = self.selectPlaintiff()

    def selectNumofInstance(self):
        '''
        #提取案件的几审信息
        :return:
        '''
        if selectNumofInstance(self.__Title):
            return selectNumofInstance(self.__Title)
        else:
            self.mkFile("几审信息出错")
            return []

    def selectCity(self):
        '''
        #提取所属市信息
        :return:
        '''
        if selectCity(self.__filecontent):
            return selectCity(self.__filecontent)
        else:
            self.mkFile("所属市查询出错")
            return []

    def selectFileType(self):
        '''
        #提取案件和文书类型
        :return:
        '''
        if selectFileType(self.__filecontent):
            return selectFileType(self.__filecontent)
        else:
            self.mkFile("案件和文本类型出错")
            return []

    def selectTime(self):
        '''
        #提取时间信息
        :return:
        '''
        if selectTime(self.__filecontent):
            return selectTime(self.__filecontent)
        else:
            self.mkFile("时间出错")
            return []

    def selectJudgmentResult(self):
        '''
        #提取判决结果
        :return:
        '''
        if selectJudgmentResult(self.__filecontent):
            return selectJudgmentResult(self.__filecontent)
        else:
            self.mkFile("判决结果出错")
            return []

    def selectDefendant(self):
        '''
        #提取被告人
        :return:
        '''
        if selectDefendant(self.__filecontent):
            return selectDefendant(self.__filecontent)
        else:
            self.mkFile("被告人出错")
            return []

    def selectRequest(self):
        '''
        #提取上诉人请求
        :return:
        '''
        if selectRequest(self.__filecontent):
            return selectRequest(self.__filecontent)
        else:
            self.mkFile("请求出错")
            return []


    def selectPlaintiff(self):
        '''
        #提取原告
        :return:
        '''
        if selectPlaintiff(self.__filecontent):
            return selectPlaintiff(self.__filecontent)
        else:
            self.mkFile("原告出错")
            return []

    def dataDeal(self):
        try:
            ErrorText = "几审报错"
            print("几审：" + self.__res0[0])
            ErrorText = "所属市报错"
            print("所属市：" + self.__res1[0])
            ErrorText = "案件类型报错"
            print("案件类型：" + self.__res2[:len(self.__res2) - 3])
            ErrorText = "文书类型报错"
            print("文书类型:" + self.__res2[len(self.__res2) - 3:])
            ErrorText = "时间报错"
            print("时间：" + self.__res3[0])
            ErrorText = "判决如下报错"
            print("判决如下" + self.__res4[0])
            ErrorText = "被告人报错"
            if len(self.__res5) != 0:
                for i in self.__res5:
                    print(i)
            print(self.__res6[0])
            if len(self.__res7) != 0:
                for i in self.__res7:
                    print(i)
        except IndexError:  # 对错误进行分类然后分别放到各自类型的错误文件夹下面
            print(ErrorText)


def clearErrorFolder(FatherPath):
    ErrorPath = os.path.join(FatherPath, "Error")
    if os.path.isdir(ErrorPath):
        shutil.rmtree(ErrorPath)

#提取几审信息
def selectNumofInstance(ChildInfo):
    res0 = re.findall(r".审", ChildInfo)
    if len(res0) == 0:
        return 0
    else:
        return res0

#提取所属市信息
def selectCity(FileText):
    res1 = re.findall(r"[\u4e00-\u9fa5]{2,5}?(?:省|自治区|市)", FileText)
    if len(res1) == 0:
        return 0
    else:
        return res1

#提取案件和文书类型
def selectFileType(FileText):
    res2 = re.findall(r"[\u4e00-\u9fa5 ]{2,}书", FileText)
    try:
        res2 = res2[0].replace(" ", "")
    except IndexError:
        return 0
    return res2

#提取时间信息
def selectTime(FileText):
    res3 = re.findall(r"[一二三四五六七八九十〇○０]{4}年?[一二三四五六七八九十]{1,3}月?[一二三四五六七八九十×]{1,3}日?", FileText)
    if len(res3) == 0:
        return 0
    else:
        return res3

#提取判决结果
def selectJudgmentResult(FileText):
    filetext = FileText.split("判决如下")
    res4 = re.findall(r'[：:；][\d\D]*?\n(?:如不服本判决|本判决|本案判决)', filetext[len(filetext) - 1])
    try:
        res4[0] = res4[0].replace("\n本判决", "")
        res4[0] = res4[0].replace("\n本案判决", "")
        res4[0] = res4[0].replace("\n如不服本判决", "")
    except IndexError:
        return 0
    return res4

#提取被告人
def selectDefendant(FileText):
    str2 = FileText.split("一案")[0]
    res5 = re.findall(r'{}[:]?.*。'''.format("被告"), str2)
    if len(res5) == 0:
        return 0
    else:
        return res5
    return res5

#提取上诉人请求
def selectRequest(FileText):
    res6 = re.findall(r"(?:请求|要求|判令)[：]?[\d\D]*?。\n(?:被告|事实|原告)", FileText)
    if len(res6):
        res6[0] = res6[0].replace("\n被告", "")
        res6[0] = res6[0].replace("\n事实", "")
        res6[0] = res6[0].replace("\n原告", "")
    else:
        return 0
    return res6

def selectPlaintiff(FileText):
    str2 = FileText.split("一案")[0]
    res7 = re.findall(r'{}[:]?.*。'''.format("原告"), str2)
    if len(res7) == 0:
        return 0
    else:
        return res7


def openFileFunc(addressPath):
    if os.path.isfile(addressPath):
        File = open(addressPath, encoding='UTF-8')
        FileText = File.read()
        return FileText
    else:
        return 0
def mkFile(rootPath,packge,Title):
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
        else:
            print("文件已存在")
def main():
    docreader = docReader()
    docwriter = docWriter()

    for childPath in os.listdir(docreader.getRootPathFunc()):
        docreader.setAddressPathFunc(os.path.join(docreader.getRootPathFunc(), childPath))
        docwriter.setTitle(childPath)
        if docreader.openFileFunc():
            if len(docreader.openFileFunc()) > 200:
                docwriter.setFileContent(docreader.openFileFunc())
                docwriter.docDeal()
                docwriter.dataDeal()
            else:
                os.remove(childPath)

main()
