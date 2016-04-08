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
            urls = config.items(book)
            bookUrl = urls[0][1]
            if len(urls) == 2:
                bookUrl = urls[1][1]
            #读取后续章节并返回最后一章的URL
            la = LoadArticle.LoadArticle()
            la.LoadBook("E:\\快盘\\闲书\\", book, bookUrl)
    except:
        info=sys.exc_info()  
        print(info[0],":",info[1])
    return