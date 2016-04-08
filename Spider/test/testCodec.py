#coding=utf-8
"""练手"""
import io
import sys
import urllib.request
import codecs

#获取网页内容
def get_html(url):
    """function to get html of url"""
    page = urllib.request.urlopen(url)
    _html = page.read()
    return _html

print(sys.stdout.encoding)

TEST = "测试"
print(TEST)

HTML = get_html("http://baike.baidu.com/subview/1234/8387432.htm")
HTML_UTF8 = HTML.decode("utf8")

#文件编码
f = open('out.txt','w',-1,'utf-8')
f.write(HTML.decode("utf8"))

