# -*- coding: utf-8 -*-
# @Time    : 2021/3/16 0016 17:08
# @Author  : YJW
# @FileName: voc_label.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
from os import getcwd

sets = ['train', 'val', 'test']
classes = [ 'RBC']   # 改成自己的类别
abs_path = os.getcwd()
print(abs_path)

def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h

def convert_annotation(image_id):
    in_file = open('./VOC2007_redcell_20210415/Annotations/%s.xml' % (image_id), encoding='UTF-8')
    out_file = open('./VOC2007_redcell_20210415//labels/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        # difficult = obj.find('difficult').text
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        b1, b2, b3, b4 = b
        # 标注越界修正
        if b2 > w:
            b2 = w
        if b4 > h:
            b4 = h
        b = (b1, b2, b3, b4)
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()
for image_set in sets:
    if not os.path.exists('./VOC2007_redcell_20210415/labels/'):
        os.makedirs('./VOC2007_redcell_20210415/labels/')
    image_ids = open('./VOC2007_redcell_20210415/ImageSets/Main/%s.txt' % (image_set)).read().strip().split()
    list_file = open('./VOC2007_redcell_20210415/%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        list_file.write(abs_path + '/VOC2007_redcell_20210415/JPEGImages/%s.jpg\n' % (image_id))
        convert_annotation(image_id)
    list_file.close()