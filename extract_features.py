import cv2
import numpy as np
import mahotas as mt
import os
import pandas as pd
from csv import DictWriter

extractAll = []

def extractHaralick(image_gray_crop):
    textures = mt.features.haralick(image_gray_crop)
    return textures.mean(axis=0)

def extractHistG(image):
    (b, g, r) = cv2.split(image)
    return cv2.calcHist([g], [0], None, [256], [0, 255])

def extractChain(image):
    ret, thresh = cv2.threshold(image, 127, 255, 0)
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    return contours

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

for dict in extractAll:
    with open('csv\extracoes.csv', 'a', newline='', encoding='utf8') as f_object:

        dictwriter_object = DictWriter(
            f_object, fieldnames=['name', 'ht_mean', 'hist_g', 'chain'], delimiter=';')

        dictwriter_object.writerow(dict)

        f_object.close()

