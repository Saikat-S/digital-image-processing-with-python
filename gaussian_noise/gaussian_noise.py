#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 00:08:36 2019

@author: saikats
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


def add_gaussain_noise(img,mean,sigma):
    # make a random gaussian noise
    gaussian_noise = np.random.normal(mean, sigma,(img.shape))
    
    #make a black image
    noisy_image = np.zeros(img.shape, img.dtype)
    
    #add goussian noise in image 
    noisy_image = img + gaussian_noise
    
    #normalize the noisy image 
    cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
    noisy_image = noisy_image.astype(np.uint8)
    
    return noisy_image
    
if __name__ == "__main__":

    img = cv2.imread('image/lena.png',0)

    img1 = add_gaussain_noise(img, 50, 2)
    img2 = add_gaussain_noise(img, 50, 8)
    img3 = add_gaussain_noise(img, 50, 16)
    img4 = add_gaussain_noise(img, 50, 32)
    img5 = add_gaussain_noise(img, 50, 64)
    
    fig = plt.figure(figsize=(10,8))
    fig.add_subplot(2,5,1)
    plt.title("Original Image")
    plt.axis('off')
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    
    fig.add_subplot(2,5,2)
    plt.title("Sigma = 2")
    plt.axis('off')
    plt.imshow(img1, cmap = 'gray', interpolation = 'bicubic')
    
    fig.add_subplot(2,5,3)
    plt.title("Sigma = 8")
    plt.axis('off')
    plt.imshow(img2, cmap = 'gray', interpolation = 'bicubic')
    
    fig.add_subplot(1,5,1)
    plt.title("Sigma = 16")
    plt.axis('off')
    plt.imshow(img2, cmap = 'gray', interpolation = 'bicubic')
    
    fig.add_subplot(1,5,2)
    plt.title("Sigma = 32")
    plt.axis('off')
    plt.imshow(img3, cmap = 'gray', interpolation = 'bicubic')
    
    fig.add_subplot(1,5,3)
    plt.title("Sigma = 64")
    plt.axis('off')
    plt.imshow(img4, cmap = 'gray', interpolation = 'bicubic')
    
    