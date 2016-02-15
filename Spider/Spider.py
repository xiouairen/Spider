#coding=utf-8
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://www.sina.com.cn")

print(html)
print(type(html))
html_utf8 = html.decode("UTF-8")
print(html_utf8)