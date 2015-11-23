# coding=UTF-8

import npextractor

import os
import os.path
import sys
inputdir = sys.argv[1]                                  # 指明被遍历的文件夹
outputdir = sys.argv[2]

if not os.path.exists(outputdir):
    os.mkdir(outputdir)
for parent,dirnames,filenames in os.walk(inputdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for filename in filenames:
        ifullpath = os.path.join(parent,filename)
        uifullpath = unicode(ifullpath , "utf8")
        print filename
        h = open(uifullpath)
        h.readline()
        h.readline()
        h.readline()
        h.readline()
        allthetext = h.read()
        h.close()
        ofullpath = os.path.join(outputdir,filename)
        uofullpath = unicode(ofullpath , "utf8")
        keywords = npextractor.extract(allthetext)
        if keywords:
            oh = open(uofullpath, 'w')
            oh.write(keywords)
            oh.close()