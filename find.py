# -*- coding: UTF-8 -*-
#
# frendyxzc@126.com
# 2017.08.28

import os
import re
import time

"""
Find files
"""
def findFiles(dir):
    IMAGE = []
    FILE = []
    COLOR = []

    startTime = time.time()

    # 三个参数：分别返回 1.父目录 2.所有文件夹名字（不含路径）3.所有文件名字
    for parent, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            if "\\build" in parent or "\\.idea" in parent or "\\.gradle" in parent:
                continue

            ext = file_extension(filename)
            if ext == ".png" or ext == ".jpg":
                IMAGE.append(os.path.join(parent, filename))
            elif ext == ".java" or ext == ".kt" or ext == ".xml":
                FILE.append(os.path.join(parent, filename))

            if "color.xml" in filename:
                COLOR.append(os.path.join(parent, filename))

    endTime = time.time()
    print("== It take %d second to find files.." % (endTime - startTime))

    return IMAGE, FILE, COLOR


def file_extension(path):
    return os.path.splitext(path)[1]


def contain(target, file):
    fopen = open(file, 'r', encoding='UTF-8')
    for line in fopen:
        if target in line:
            fopen.close()
            return True

    fopen.close()
    return False


def containImage(target, file):
    name = os.path.basename(target).split(".")[0]
    return contain(name, file)


def containOne(list, content):
    for item in list:
        if item in content:
            return True

    return False

"""
Find colors
"""
def findColors(colorFiles):
    startTime = time.time()
    COLOR = []

    for colorFile in colorFiles:
        fopen = open(colorFile, 'r', encoding='UTF-8')
        content = fopen.read()
        pattern_key = re.compile(r'<color name="(.+?)">', re.S)
        COLOR += re.findall(pattern_key, content)
        fopen.close()

    endTime = time.time()
    print("== It take %d second to find colors.." % (endTime - startTime))

    return COLOR