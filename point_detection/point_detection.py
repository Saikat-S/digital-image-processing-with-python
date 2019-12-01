#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 00:37:21 2019

@author: saikats
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#read image with opencv2
def readImg():
    img = cv2.imread('image/point.png',0)
    return img

#apply the kernel to the image
def getPixel(img, kr, i, j):
    pixel = 0
    x = i-1
    y = j-1
    for ii in range(3):
        for jj in range(3):
           pixel = pixel + (kr[ii][jj] * img[x+ii][y+jj]) 
    return pixel

#point detection function read image and return point detected image
def pointDetect(img):
   kr = [[1,1,1], [1,-8,1], [1,1,1]]
   
   rows , cols = img.shape
   
   new_img = np.zeros(img.shape, img.dtype)
   
   for i in range(rows-1):
       for j in range(cols-1):
           if(i>0 and j>0):
               pixel = getPixel(img, kr, i, j)
               
               if pixel > 170:
                   new_img[i][j] = 255
               
   
   return new_img

if __name__ == "__main__":
    
   img = readImg()
   
   new_img = pointDetect(img)

   #show images in matplot   
   fig = plt.figure(figsize=(9,9))
   fig.add_subplot(1,2,1)
   plt.title('Original img')
   plt.axis('off')
   plt.imshow(img, cmap='gray', interpolation='bicubic')
   
   fig.add_subplot(1,2,2)
   plt.title('Original img')
   plt.axis('off')
   plt.imshow(new_img, cmap='gray', interpolation='bicubic')
   