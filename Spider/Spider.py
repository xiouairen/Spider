#coding=utf-8
import io
import sys
import configparser
import LoadArticle

def downloadBooks():
    configFilePath = "conf.ini"
    config = configparser.ConfigParser()
    config.read(configFilePath)
    books = config.sections()
    try:
        for book in books:
            sites = config.items(book)
            for site in sites:
                siteName = site[0]
                bookUrl = site[1]
                #读取后续章节并返回最后一章的URL
                la = LoadArticle.LoadArticle()
                la.LoadBook("E:\\快盘\\闲书\\", siteName, book, bookUrl)
    except:
        info = sys.exc_info()  
        print(info[0],":",info[1])
    return