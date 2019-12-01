#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:39:05 2019

@author: saikats
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def set_bit(num, pos):
  mask = 1 << pos
  num &= ~mask
  return num



if __name__ == "__main__":

    img1 = cv2.imread('image/image.jpg',0)

    img = np.zeros(img1.shape, img1.dtype)
    
    rows, cols = img1.shape

    fig = plt.figure(figsize=(20,10))
    
    for i in range(rows):
            for j in range(cols):
                img[i][j] = img1[i][j]
    
    fig.add_subplot(2,9,1)
    plt.title("Orignal Image")
    plt.axis('off')
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')        
    
    p = 2
    pp = 2
    b = 7
    while(b>=1):
        img = np.zeros(img1.shape, img1.dtype)
        for i in range(rows):
            for j in range(cols):
                pixel = img1[i][j]
                c = 7 - b + 1
                cc = 7
                while(c>0): 
                    pixel = set_bit(pixel,cc)
                    cc = cc-1
                    c = c - 1
                img[i][j] = pixel
        
        fig.add_subplot(pp,9,p)
        plt.title('bit plane = {}'.format(b))
        plt.axis('off')
        plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')        
        p = p + 1  
        
        if(p>4):
            p = 1
            pp = 1
        
        b = b-1

