#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:41:49 2019

@author: saikats
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


def readImg():
    img = cv2.imread('image/image.png')
    return img

if __name__ == "__main__":
    
    img = readImg()
    
    #Dialation
    kernel = np.ones((5,5), np.uint8)
    dilation = cv2.dilate(img, kernel, iterations=1)
    
    #Erosion
    erosion = cv2.erode(img, kernel, iterations=1)
    
    #Opening
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    
    #Closing 
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    
    #Morphological Gradient
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    
    #Top Hat
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    
    #Black Hat
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    
    fig = plt.figure(figsize=(20,13))
    fig.add_subplot(2,8,1)
    plt.title('Original')
    plt.axis('off')
    plt.imshow(img, cmap='gray',interpolation='bicubic')
    
    
    fig.add_subplot(2,8,2)
    plt.title('Dialation')
    plt.axis('off')
    plt.imshow(dilation, cmap='gray', interpolation='bicubic')
    
    fig.add_subplot(2,8,3)
    plt.title('Erosion')
    plt.axis('off')
    plt.imshow(erosion, cmap='gray', interpolation='bicubic')
    
    fig.add_subplot(2,8,4)
    plt.title('Opening')
    plt.axis('off')
    plt.imshow(opening, cmap='gray', interpolation='bicubic')
    
    fig.add_subplot(1,8,1)
    plt.title('Closing')
    plt.axis('off')
    plt.imshow(closing, cmap='gray', interpolation='bicubic')
    
    fig.add_subplot(1,8,2)
    plt.title('Gradient')
    plt.axis('off')
    plt.imshow(gradient, cmap='gray', interpolation='bicubic')
    
    fig.add_subplot(1,8,3)
    plt.title('Top Hat')
    plt.axis('off')
    plt.imshow(tophat, cmap='gray', interpolation='bicubic')
    
    fig.add_subplot(1,8,4)
    plt.title('Black Hat')
    plt.axis('off')
    plt.imshow(blackhat, cmap='gray', interpolation='bicubic')
    
    