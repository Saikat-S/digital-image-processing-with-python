#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 13:13:06 2019

@author: saikats
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


def readImg():
    img = cv2.imread('image/line.png',0)
    return img

def getPixel(img, kr, i, j):
    pixel = 0
    x = i-1
    y = j-1
    for ii in range(3):
        for jj in range(3):
           pixel = pixel + (kr[ii][jj] * img[x+ii][y+jj]) 
    return pixel

def lineDetect(img):
   kr1 = [[-1,-1,-1], [2,2,2], [-1,-1,-1]] #horizontal kernel
   kr2 = [[2,-1,-1], [-1,2,-1], [-1,-1,2]] #+45 kernel
   kr3 = [[-1,2,-1], [-1,2,-1], [-1,2,-1]] #vertical kernel
   kr4 = [[-1,-1,2], [-1,2,-1], [2,-1,-1]] #-45 kernel
   
   rows , cols = img.shape
   
   new_img = np.zeros(img.shape, img.dtype)
   
   for i in range(rows-1):
       for j in range(cols-1):
           if(i>0 and j>0):
               pixel = getPixel(img, kr1, i, j)
               if pixel > 255:
                   new_img[i][j] = 255
               pixel = getPixel(img, kr2, i, j)
               if pixel > 255:
                   new_img[i][j] = 255
               pixel = getPixel(img, kr3, i, j)
               if pixel > 255:
                   new_img[i][j] = 255
               pixel = getPixel(img, kr4, i, j)
               if pixel > 255:
                   new_img[i][j] = 255
   
   return new_img

if __name__ == "__main__":
   img = readImg()
   
   new_img = lineDetect(img)

   
   fig = plt.figure(figsize=(9,9))
   fig.add_subplot(1,2,1)
   plt.title('Original Image')
   plt.axis('off')
   plt.imshow(img, cmap='gray', interpolation='bicubic')
   
   fig.add_subplot(1,2,2)
   plt.title('Line Detected Image')
   plt.axis('off')
   plt.imshow(new_img, cmap='gray', interpolation='bicubic')
   