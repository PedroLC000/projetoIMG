import cv2
import numpy as np
import mahotas as mt
import os
import pandas as pd
from csv import DictWriter
import csv

extractAll = []

def extractHaralick(image_gray_crop):
    textures = mt.features.haralick(image_gray_crop)
    textures_str = str(textures.mean(axis=0))
    x = textures_str.replace("\n", "")
    return x

def extractHistG(image):
    (b, g, r) = cv2.split(image)
    g_str = str(cv2.calcHist([g], [0], None, [256], [0, 255]))
    y = g_str.replace("\n", "")
    return y

def extractChain(image):
    ret, thresh = cv2.threshold(image, 127, 255, 0)
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    a = []
    for i in contours:
        contours_str = str(i)
        z = contours_str.replace("\n", "")
        a.append(z)
    return a

for filename in os.scandir('saves\crop'):
    extract = {}
    if filename.is_file():
        image_gray_crop = cv2.imread(filename.path, 0)
        image_RGB_crop = cv2.imread(filename.path)
        extract['name'] = filename.name
        extract['ht_mean'] = extractHaralick(image_gray_crop)
        extract['hist_g'] = extractHistG(image_RGB_crop)
        extract['chain'] = extractChain(image_gray_crop)
        extractAll.append(extract)

with open('csv\output.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'ht_mean', 'hist_g', 'chain']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(extractAll)

# for dict in extractAll:
#     with open('csv\extracoes.csv', 'a', newline='', encoding='utf8') as f_object:

#         dictwriter_object = DictWriter(
#             f_object, fieldnames=['name', 'ht_mean', 'hist_g', 'chain'], delimiter=';')

#         dictwriter_object.writerow(dict)

#         f_object.close()

