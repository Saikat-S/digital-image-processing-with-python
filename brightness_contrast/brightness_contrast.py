#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:55:32 2019

@author: saikats
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    img = cv2.imread('image/cameraman.jpeg',0)

    alpha = float(input('Enter the contrast (1-3) : '))
    beta = int(input('Enter the brightness (1-100) : '))


    rows,cols = img.shape

    new_img = np.zeros(img.shape, img.dtype)
    new_img1 = np.zeros(img.shape, img.dtype)
    new_img2 = np.zeros(img.shape, img.dtype)

    mn_pixel = 1000
    mx_pixel = 0
    total_pixel = 0
    cnt_pixel = 0


    #for brightness and contrast control 
    # g[i,j] = alpha * f[i,j] + beta
    for i in range(rows):
        for j in range(cols):
            pixel = img[i][j]
            total_pixel+=pixel
            cnt_pixel = cnt_pixel + 1
            if pixel>mx_pixel:
                mx_pixel = pixel
            elif pixel<mn_pixel:
                mn_pixel = pixel
       

    bri = total_pixel/cnt_pixel
    con = mx_pixel - mn_pixel

    print('Max Pixel : ',mx_pixel)
    print('Min Pixel : ',mn_pixel)
    print('Brightness : ',bri)
    print('Contrast : ', con)

    # for both brightness and contrast change
    for i in range(rows):
        for j in range(cols):
            pixel = img[i][j] * alpha + beta
            if pixel>255:
                pixel = 255
            new_img[i,j] = pixel
    

    #for brightness control
    for i in range(rows):
        for j in range(cols):
            pixel = img[i,j]
            pixel= pixel + beta
            pixel = pixel%256
            new_img1[i,j] = pixel


    #for contrast control
    change = mx_pixel-alpha*100 
          
    for i in range(rows):
        for j in range(cols):
            pixel = img[i,j]
            if pixel<change:
                pixel = change
                pixel = pixel%256
                new_img2[i,j] = pixel

    fig = plt.figure(figsize=(10,9))
    fig.add_subplot(1,4,1)
    plt.title("Original")
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')

    fig.add_subplot(1,4,2)
    plt.title("New Image")
    plt.imshow(new_img, cmap = 'gray', interpolation = 'bicubic')

    fig.add_subplot(1,4,3)
    plt.title("Change Brightness")
    plt.imshow(new_img1, cmap = 'gray', interpolation = 'bicubic')

    fig.add_subplot(1,4,4)
    plt.title("Change Contrast")
    plt.imshow(new_img2, cmap = 'gray', interpolation = 'bicubic')