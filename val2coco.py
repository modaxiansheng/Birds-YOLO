# -*- coding: utf-8 -*-
# @Time    : 2021/3/17 0017 10:55
# @Author  : YJW
# @FileName: val2coco.py
# @Software: PyCharm
import os
import random
from shutil import copyfile
in_dir="VOC2007_redcell_20210415"
out_dir="coco2007_redcell_20210415"
# with open(os.path.join(in_dir,"train.txt")) as f:
#     for item in f.read().split("\n"):
#         inimage=item
#         inlabel=item.split("JPEGImages")[0]+"labels"+item.split("JPEGImages")[1].split(".jpg")[0]+".txt"
#         outimage=item.split("VOC2007_redcell_20210415")[0] +out_dir+"/images/train2007"+item.split("VOC2007_redcell_20210415")[1].split("JPEGImages")[1]
#         outlabel=item.split("VOC2007_redcell_20210415")[0] +out_dir+"/labels/train2007"+item.split("VOC2007_redcell_20210415")[1].split("JPEGImages")[1].split(".jpg")[0]+".txt"
#         copyfile(inimage, outimage)
#         copyfile(inlabel, outlabel)
#         print(inimage)
#         print(inlabel)
#         print(outimage)
#         print(outlabel)

with open(os.path.join(in_dir,"val.txt")) as f:
    for item in f.read().split("\n"):
        inimage = item
        inlabel = item.split("JPEGImages")[0] + "labels" + item.split("JPEGImages")[1].split(".jpg")[0] + ".txt"
        outimage = item.split("VOC2007_redcell_20210415")[0] + out_dir + "/images/val2007" + item.split("VOC2007_redcell_20210415")[1].split("JPEGImages")[1]
        outlabel = item.split("VOC2007_redcell_20210415")[0] + out_dir + "/labels/val2007" + item.split("VOC2007_redcell_20210415")[1].split("JPEGImages")[1].split(".jpg")[0] + ".txt"
        print(inimage)
        print(inlabel)
        print(outimage)
        print(outlabel)
        # copyfile(inimage, outimage)
        copyfile(inlabel, outlabel)
# with open(os.path.join(in_dir, "test.txt")) as f:
#     for item in f.read().split("\n"):
#         inimage = item
#         inlabel = item.split("JPEGImages")[0] + "labels" + item.split("JPEGImages")[1].split(".jpg")[0] + ".txt"
#         outimage = item.split("VOC2007_redcell_20210415")[0] + out_dir + "/images/test2017" + \
#                    item.split("VOC2007_redcell_20210415")[1].split("JPEGImages")[1]
#         outlabel = item.split("VOC2007_redcell_20210415")[0] + out_dir + "/labels/test2017" + \
#                    item.split("VOC2007_redcell_20210415")[1].split("JPEGImages")[1].split(".jpg")[0] + ".txt"
#         print(inimage)
#         print(inlabel)
#         print(outimage)
#         print(outlabel)
#         copyfile(inimage, outimage)
# copyfile(inlabel, outlabel)