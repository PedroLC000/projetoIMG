import cv2
import numpy as np
import mahotas as mt
import os
import pandas as pd
import shutil

for f in os.scandir('saves\crop'):
    os.remove(f)

for cont, filename in enumerate(os.scandir('frames')):

    if filename.is_file():

        image = cv2.imread(filename.path)
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
        # método de segmentação de imagem Canny
        blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
        wide = cv2.Canny(blurred, 10, 200)

        # detecta contornos na imagem binarizada usando cv2.CHAIN_APPROX_NONE
        contours, hierarchy = cv2.findContours(image=wide, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

        image_copy = image.copy()

        # directory = "crop"+str(cont)
        # parent_dir = "saves\crop"
        # path = os.path.join(parent_dir, directory)
        # os.mkdir(path)

        # utilizado para extrair cada imagem encontrada com o algoritmo de fremman
        for count, contour_line in enumerate(contours):
            x, y = [], []
            if len(contour_line) > 80:
                for contour in contour_line:
                    x.append(contour[0][0])
                    y.append(contour[0][1])

                x1, x2, y1, y2 = min(x), max(x), min(y), max(y)
                cropped = image[y1:y2, x1:x2]

                cv2.imwrite(f'saves/crop/Frame{cont}-crop{count}.png', cropped)
                x.clear()
                y.clear()