#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 23:31:23 2019

@author: saikats
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    img1 = cv2.imread('image/full_image.png',0)
    img2 = cv2.imread('image/part_image.png',0)

    img = np.zeros(img1.shape, img1.dtype)

    rows, cols = img1.shape

    for i in range(rows):
        for j in range(cols):
            img[i,j] = img1[i,j] - img2[i,j]   
      

    fig = plt.figure(figsize=(10,9))
    fig.add_subplot(1,3,1)
    plt.title("Full Image")
    plt.imshow(img1, cmap = 'gray', interpolation = 'bicubic')
    
    fig.add_subplot(1,3,2)
    plt.title("Object Image")
    plt.imshow(img2, cmap = 'gray', interpolation = 'bicubic')

    fig.add_subplot(1,3,3)
    plt.title("New Image")
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')

    #write image
    cv2.imwrite('image/output.png',img)
