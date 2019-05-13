import docReader
import docWriter



class fileReader:
    def get_localizer(self, fileType = "txt"):
        FileType = dict(txt=txtWRer, hadoop=hadoopWRer)
        return FileType[fileType]()


class txtWRer(docWriter.docWriter, docReader.txtReader):
    __res0 = []
    __res1 = []
    __res2 = []
    __res3 = []
    __res4 = []
    __res5 = []
    __res6 = []
    __res7 = []
    __res8 = []

    def openFile(self):
        for title in self.getFileNameFunc():
            self._openFileFunc(title)

    def docDealFunc(self):
        for title in self.getFileNameFunc():
            self.setTitle(title)
            self.setFileContent(self._openFileFunc(title))
            self.__docDeal()
            self.__dataDeal()

    def __docDeal(self):
        self.__res0, self.__res1, self.__res2, self.__res3, self.__res4, self.__res5, self.__res6, self.__res7, \
            self.__res8 = self._docDealFunc()

    def __dataDeal(self):
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
            self.mkFile(self.getTitle(), ErrorText)


class hadoopWRer(docWriter.docWriter, docReader.hadoopReader):
    pass
