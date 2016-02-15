#coding=utf-8
"""练手"""
import io
import sys
import urllib.request
import codecs

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

f = codecs.open('out.txt','a','utf-8')
f.write(HTML.decode("utf8"))

