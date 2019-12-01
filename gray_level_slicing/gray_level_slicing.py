#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:26:00 2019

@author: saikats
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    img1 = cv2.imread('image/image.jpg',0)
    
    img = np.zeros(img1.shape, img1.dtype)

    rows, cols = img1.shape

    mx = 0

    for i in range(rows):
        for j in range(cols):
            mx = max(mx, img1[i][j])

    c = 255/(np.log(1 + mx))

    for i in range(rows):
        for j in range(cols):
            img[i][j] = c * np.log(1+img1[i][j]) 
      
      
        
    fig = plt.figure(figsize=(8,5))
    fig.add_subplot(1,2,1)
    plt.title("Image")
    plt.axis('off')
    plt.imshow(img1, cmap = 'gray', interpolation = 'bicubic')

    fig.add_subplot(1,2,2)
    plt.title("Log Transformation")
    plt.axis('off')
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')

    #write image
    cv2.imwrite('image/output.png',img)