# -*- coding: utf-8 -*-
import os
import shutil
import re
#初始读取文件进行大地区分类
def RedaFile(FatherPath,address):
    '''

    :param FatherPath: 读取文件的根目录
    :param address: 读取地区的名字，例如重庆
    :return: 会在根目录下创建address名的文件夹，并把算法抓不出来的任何地区信息的文件放进错误文件夹
    '''
    ''' 功能是什么；具体实现人过程，参数的作用；那个人，什么时候写的，修改人，修改时间'''
    i = 0
    for Childinfo in os.listdir(FatherPath + 'minshi'):
        info = os.path.join(FatherPath + 'minshi',Childinfo)
        start = open(info,encoding='UTF-8')
        fileLine = start.readline()
        interimLocation = re.findall(r'.*法院',fileLine)
        try:
            while len(interimLocation) == 0:
                fileLine = start.readline()
                interimLocation = re.findall(r'.*法院', fileLine)
        except EOFError:
            ErrorPath = os.path.join(FatherPath, "文件分地区读取错误")
            if not os.path.isdir(ErrorPath):
                try:
                    os.makedirs(ErrorPath)
                except NotADirectoryError:
                    print("创建分地区错误文件夹出错")
            ErrorFile = os.path.join(ErrorPath,Childinfo)
            if not os.path.isfile(ErrorFile):
                start.close()
                try:
                    shutil.move(info, ErrorFile)
                except OSError:
                    print("转移错误文件出错")
            else:
                print("错误文件已存在，覆盖")
                os.remove(ErrorFile)
                try:
                    shutil.move(info, ErrorFile)
                except OSError:
                    print("转移错误文件出错")
        if len(interimLocation):
            Location = re.findall(r'' + address, interimLocation[0])
            if len(Location):
                ChangePath = os.path.join(FatherPath, Location[0])
                if not os.path.isdir(ChangePath):
                    try:
                        os.makedirs(ChangePath)
                    except NotADirectoryError:
                        print("Error:"+ChildPath+"!!!!!!!!!!!!!!!!")
                ChildPath = os.path.join(ChangePath, Childinfo)
                print(ChildPath)
                if not os.path.isfile(ChildPath):
                    start.close()
                    try:
                        shutil.move(info, ChildPath)
                    except OSError:
                        print("Error:" + ChildPath + "!!!!!!!!!!!!!!!!")
                    i = i+1
                else:
                    print("文件已存在,自动覆盖")
                    os.remove(ChildPath)
                    try:
                        shutil.move(info, ChildPath)
                    except OSError:
                        print("Error:" + ChildPath + "!!!!!!!!!!!!!!!!")
                    i = i+1
    print("文件个数："+str(i))

def clearErrorFolder(FatherPath):
    ErrorPath = os.path.join(FatherPath,"Error" )
    if os.path.isdir(ErrorPath):
        shutil.rmtree(ErrorPath)

#测试功能函数
def test(FatherPath):
    info = os.path.join(FatherPath + '重庆',"一建公司与聚金公司建设工程施工合同纠纷二审民事判决书.txt")
    File = open(info, encoding='UTF-8')
    FileText = File.read()

#提取几审信息
def selectNumofInstance(ChildInfo):
    res0 = re.findall(r".审", ChildInfo)
    return res0

#提取所属市信息
def selectCity(FileText):
    res1 = re.findall(r"[\u4e00-\u9fa5]{2,5}?(?:省|自治区|市)",FileText)
    return res1

#提取案件和文书类型
def selectFileType(FileText):
    newres2 = re.findall(r"[\u4e00-\u9fa5 ]{2,}书", FileText)
    res2 = newres2[0].replace(" ", "")
    return res2

#提取时间信息
def selectTime(FileText):
    res3 = re.findall(r"[\u4e00-\u9fa5〇○]{4}年?[\u4e00-\u9fa5]{1,3}月?[\u4e00-\u9fa5×]{1,3}日?", FileText)
    return res3

#提取判决结果
def selectJudgmentResult(FileText):
    filetext = FileText.split("判决如下")
    print(filetext[len(filetext) - 1])
    res4 = re.findall(r'[：:；][\d\D]*?\n(?:如不服本判决|本判决|本案判决)', filetext[len(filetext) - 1])
    try:
        res4[0] = res4[0].replace("\n本判决", "")
        res4[0] = res4[0].replace("\n本案判决", "")
        res4[0] = res4[0].replace("\n如不服本判决", "")
    except IndexError:
        print(FileText)
    return res4

#提取被告人
def selectDefendant(FileText):
    res5 = re.findall(r'{}[^。]*?。'.format("\n被上诉人"), FileText)
    return res5

#提取上诉人请求
def selectRequest(FileText):
    res6 = re.findall(r"{}[\d\D]*?\n".format("请求:"),FileText)
    if len(res6):
        print("请求为：" + res6)
    else:
        print(FileText)

def DealChongQing(FatherPath,address):
    clearErrorFolder(FatherPath)
    for ChildInfo in os.listdir(FatherPath + address):
        info = os.path.join(FatherPath + address, ChildInfo)
        print(info)

        File = open(info,encoding='UTF-8')
        FileText = File.read()

        res0 = selectNumofInstance(ChildInfo)

        res1 = selectCity(FileText)

        res2 = selectFileType(FileText)

        res3 = selectTime(FileText)

        res4 = selectJudgmentResult(FileText)

        res5 = selectDefendant(FileText)

        #res6 = selectRequest(FileText)

        try:
            ErrorText = "几审报错"
            print("几审：" + res0[0])
            ErrorText = "所属市报错"
            print("所属市：" + res1[0])
            ErrorText = "案件类型报错"
            print("案件类型：" + res2[:len(res2) - 3])
            ErrorText = "文书类型报错"
            print("文书类型:" + res2[len(res2) - 3:])
            ErrorText = "时间报错"
            print("时间：" + res3[0])
            ErrorText = "判决如下报错"
            print("判决如下" + res4[0])
            ErrorText = "被告人报错"
            if len(res5) != 0:
                for i in res5:
                    print(i)
            #print("请求：" + res6[0])
        except IndexError:#对错误进行分类然后分别放到各自类型的错误文件夹下面
            ChangePath = os.path.join(FatherPath+"Error", ErrorText)
            if not os.path.isdir(ChangePath):
                try:
                    os.makedirs(ChangePath)
                except NotADirectoryError:
                    print("Error:"+ErrorText+"!!!!!!!!!!!!!!!!")
            ChildPath = os.path.join(ChangePath, ChildInfo)
            print(ChildPath)
            if not os.path.isfile(ChildPath):
                File.close()
                try:
                    shutil.copy(info, ChildPath)
                except OSError:
                    print("Error:" + ChildPath + "!!!!!!!!!!!!!!!!")
            else:
                print("文件已存在")

def main():
    FatherPath = 'E:\\python\\FileAnalyse\\'
    DealChongQing(FatherPath,"重庆")










