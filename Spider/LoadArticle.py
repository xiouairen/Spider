#coding=utf-8
"""读取指定的文章并保存至同名目录下"""

import os
import configparser
import ParseHtml1

class LoadArticle:
    def __init__(self):
        self.configFilePath = ""
        self.configSection = "config"
        self.configOptionCounter = "counter"
        self.config = configparser.ConfigParser()
        return

    def InitConfig(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

        self.configFilePath = folder + "\\conf.ini"    
        if not os.path.exists(self.configFilePath):
            chapterCounter = 0
            self.config.add_section(self.configSection)
            self.config.set(self.configSection, self.configOptionCounter, str(chapterCounter))
            self.config.write(open(self.configFilePath, "w"))

        self.config.read(self.configFilePath)
        return

    def LoadOneChapter(self, folder, url):
        tp = ParseHtml1.URLParser()
        output = tp.parseHtml(url)
        nextUrl = output[0]
        title = output[1]
        content = output[2]

        chapterCounter = self.config.get(self.configSection, self.configOptionCounter)
        filePath = folder + "\\" + chapterCounter + ".txt"
    
        fp = open(filePath, "w", -1, 'utf8')
        fp.write(title.decode("utf8"))
        fp.write("\n")
        fp.write(content.decode("utf8"))
        fp.close()

        self.config.set(self.configSection, chapterCounter, url)
        if nextUrl != url:
            chapterCounter = str(int(chapterCounter)+1)
            self.config.set(self.configSection, self.configOptionCounter, chapterCounter)
            self.config.set(self.configSection, chapterCounter, nextUrl)
        self.config.write(open(self.configFilePath, "w"))
        return nextUrl

    def LoadBook(self, folder, bookName, firstUrl):
        self.InitConfig(folder+bookName)
        chapterCounter = self.config.get(self.configSection, self.configOptionCounter)
        if int(chapterCounter) == 0:
            url = firstUrl
        else:
            url = self.config.get(self.configSection, chapterCounter)
        
        nextUrl = self.LoadOneChapter(folder+bookName, url)
        while url != nextUrl:
            url = nextUrl
            nextUrl = self.LoadOneChapter(folder+bookName, url)
        return