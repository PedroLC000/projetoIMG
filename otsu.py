#Blibiotecas
import cv2 as cv
import numpy as np
import glob
from matplotlib import pyplot as plt

# Obtém todos os arquivos da pasta
folder = 'frames/*'
frames_file_list = glob.glob(folder)

# Lê a imagem e converte para grayscale
img = cv.imread(frames_file_list[70], 0)

# Threshold c/ método otsu
ret, th = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

