#coding=utf-8
import io
import sys
import configparser  

cf = configparser.ConfigParser()
cf.read("conf.ini")
  
sections = cf.sections()  
print("sections:", sections)
  
for section in sections:
    options = cf.options(section)
    print("options:", options)
    values = cf.items(section)
    print("values:", values)