# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:37:16 2019

@author: INTEL
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pytesseract
from PIL import Image

img = cv2.imread('result/test_1.png')
print(img.shape)
##灰度化处理
def grayImg(img):
    # 转化为灰度图
    gray = cv2.resize(img, (img.shape[1] * 3, img.shape[0] * 3), interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    #otsu二值化操作
    retval, gray = cv2.threshold(gray, 100, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
    return gray

#画出框选区域，0-769是宽的范围，980-1100是长的范围
cv2.drawContours(img, [np.array([[  769, 1100],
                                 [   0, 1100],
                                 [   0,    980],
                                 [  769,    980]])], 0, (0, 255, 0), 2)


    
#idImg = grayImg(img[980:1100, 0:769]) #对截取部分做灰度化处理

idImg = img[980:1100, 0:769]
cv2.imwrite("idImg.png", idImg)
pytesseract.image_to_string(idImg,  lang='deu')
cv2.imwrite("contours.png", img)