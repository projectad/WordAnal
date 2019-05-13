import os
import shutil
import re
class docWriter:
    # 文本内容
    __filecontent = ''
    # 标题内容
    __Title = ''
    __res0 = []
    __res1 = []
    __res2 = []
    __res3 = []
    __res4 = []
    __res5 = []
    __res6 = []
    __res7 = []
    __res8 = []
    def mkFile(self, packge='', root = 'E:\\python\\FileAnalyse\\裁判文书样本'):
        mkFile(root, packge, self.__Title)

    def setFileContent(self, FileContent):
        self.__filecontent = FileContent



    def setTitle(self, Title):
        self.__Title = Title

    def docDeal(self):
        self.__res0 = self.getNumofInstance()
        self.__res1 = self.getCity()
        self.__res2 = self.getFileType()
        self.__res3 = self.getTime()
        self.__res4 = self.getJudgmentResult()
        self.__res5 = self.getDefendant()
        self.__res6 = self.getRequest()
        self.__res7 = self.getPlaintiff()
        self.__res8 = self.getShiQu()

    def getNumofInstance(self):
        '''
        #提取案件的几审信息
        :return:
        '''
        if getNumofInstance(self.__Title):
            self.mkFile(getNumofInstance(self.__Title)[0])
            return getNumofInstance(self.__Title)
        else:
            return []

    def getCity(self):
        '''
        #提取所属市信息
        :return:
        '''
        if getCity(self.__filecontent):
            return getCity(self.__filecontent)
        else:
            return []

    def getFileType(self):
        '''
        #提取案件和文书类型
        :return:
        '''
        if getFileType(self.__Title):
            self.mkFile(getFileType(self.__Title)[0])
            self.mkFile(getFileType(self.__Title)[1])
            return getFileType(self.__Title)
        else:
            return []

    def getTime(self):
        '''
        #提取时间信息
        :return:
        '''
        if getTime(self.__filecontent):
            timeStr = getTime(self.__filecontent)[0]
            a = timeStr[3]
            if a == '五':
                self.mkFile("2015")
            else:
                self.mkFile("15年以后")
            return getTime(self.__filecontent)
        else:
            return []

    def getJudgmentResult(self):
        '''
        #提取判决结果
        :return:
        '''
        if getJudgmentResult(self.__filecontent):
            return getJudgmentResult(self.__filecontent)
        else:
            return []

    def getDefendant(self):
        '''
        #提取被告人
        :return:
        '''
        if getDefendant(self.__filecontent):
            return getDefendant(self.__filecontent)
        else:
            return []

    def getRequest(self):
        '''
        #提取上诉人请求
        :return:
        '''
        if getRequest(self.__filecontent):
            return getRequest(self.__filecontent)
        else:
            return []

    def getShiQu(self):
        if getShiQu(self.__Title):
            self.mkFile(getShiQu(self.__Title)[0])
            return getShiQu(self.__Title)
        else:
            return []

    def getPlaintiff(self):
        '''
        #提取原告
        :return:
        '''
        if getPlaintiff(self.__filecontent):
            return getPlaintiff(self.__filecontent)
        else:
            return []
    
    
    
    def dataDeal(self):
        try:
            ErrorText = "几审报错"
            print("几审：" + self.__res0[0])
            ErrorText = "所属市报错"
            print("所属市：" + self.__res1[0])
            ErrorText = "案件类型报错"
            print("案件类型：" + self.__res2[1])
            ErrorText = "文书类型报错"
            print("文书类型:" + self.__res2[0])
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
            self.mkFile(ErrorText)

#提取几审信息
def getNumofInstance(ChildInfo):
    res0 = re.findall(r".审", ChildInfo)
    if len(res0) == 0:
        return 0
    else:
        return res0

def getShiQu(ChileInfo):
    str = ChileInfo.split("重庆")
    for astr in str:
        res8 = re.findall(r"[市与].*?区", astr)
        if len(res8) != 0:
            res8[0] = res8[0].replace("市", "")
            res8[0] = res8[0].replace("与", "")
            return res8
    return 0

#提取所属市信息
def getCity(FileText):
    res1 = re.findall(r"[\u4e00-\u9fa5]{2,5}?(?:省|自治区|市)", FileText)
    if len(res1) == 0:
        return 0
    else:
        return res1

#提取案件和文书类型
def getFileType(ChildInfo):
    res = re.findall(r"[\d\D]{2}书", ChildInfo)
    res2 = ['', '']
    res2[0] = res[0]
    res = re.findall(r'民事|刑事', ChildInfo)
    res2[1] = res[0]
    return res2

#提取时间信息
def getTime(FileText):
    res3 = re.findall(r"[一二三四五六七八九十〇○◯０]{4}年?[一二三四五六七八九十]{1,3}月?[一二三四五六七八九十×]{1,3}日?", FileText)
    if len(res3) == 0:
        return 0
    else:
        return res3

#提取判决结果
def getJudgmentResult(FileText):
    filetext = FileText.split("判决如下")
    res4 = re.findall(r'[：:；][\d\D]*?\n(?:如不服本判决|本判决|本案判决)', filetext[len(filetext) - 1])
    try:
        res4[0] = res4[0].replace   ("\n本判决", "")
        res4[0] = res4[0].replace("\n本案判决", "")
        res4[0] = res4[0].replace("\n如不服本判决", "")
    except IndexError:
        return 0
    return res4

#提取被告人
def getDefendant(FileText):
    str2 = FileText.split("一案")[0]
    res5 = re.findall(r'{}[:]?[\d\D]*。'''.format("被告"), str2)
    if len(res5) == 0:
        return 0
    else:
        return res5
    return res5

#提取上诉人请求
def getRequest(FileText):
    res6 = re.findall(r"(?:请求|要求|判令)[：]?[\d\D]*?。\n(?:被告|事实|原告)", FileText)
    if len(res6):
        res6[0] = res6[0].replace("\n被告", "")
        res6[0] = res6[0].replace("\n事实", "")
        res6[0] = res6[0].replace("\n原告", "")
    else:
        return 0
    return res6

def getPlaintiff(FileText):
    str2 = FileText.split("一案")[0]
    res7 = re.findall(r'{}[:]?[\d\D]*。'''.format("原告"), str2)
    if len(res7) == 0:
        return 0
    else:
        return res7


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
