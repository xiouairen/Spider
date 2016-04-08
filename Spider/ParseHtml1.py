#coding=utf-8
"""解析http://www.20xs.cc的网页"""

import urllib.request
import urllib.parse
from html.parser import HTMLParser

class URLParser(HTMLParser): 
    def __init__(self): 
        self.taglevels = [] 
        self.handledtags = ["a", "h1", "div"]
        self.processing = None 
        self.nextUrl = ""
        self.catalogUrl = ""
        self.title = ""
        self.content = ""
        self.data = ""
        HTMLParser.__init__(self) 

    def handle_starttag(self,tag,attrs): 
        if tag == "a":
            for name,value in attrs:
                if name == "href":
                    self.processing = tag
                    self.data = value
        elif tag == "h1":
            self.processing = tag
        elif tag == "div":
            for name,value in attrs:
                if name == "id" and value == "book_text":
                    self.processing = tag
                elif self.processing == tag:
                    self.processing = None

    def handle_data(self,data): 
        if self.processing == "a" and data == "下一章":
            self.nextUrl = self.data
        elif self.processing == "a" and data == "返回目录":
            self.catalogUrl = self.data
        elif self.processing == "h1":
            self.title = data
        elif self.processing == "div":
            self.content += data

    def handle_endtag(self,tag): 
        if tag == self.processing:
            self.processing = None

    def parseHtml(self,url):        
        page = urllib.request.urlopen(url)        
        self.feed(page.read().decode("GBK"))
        catalogUrl = urllib.parse.urljoin("http://www.20xs.cc/", self.catalogUrl)
        nextUrl = urllib.parse.urljoin(catalogUrl, self.nextUrl)
        if self.nextUrl == self.catalogUrl:
            nextUrl = url        
        ret = [nextUrl, self.title.encode("utf8"), self.content.encode("utf8")]
        return ret
