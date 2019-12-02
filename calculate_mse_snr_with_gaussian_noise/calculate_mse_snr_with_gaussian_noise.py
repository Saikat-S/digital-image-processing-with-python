#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 01:06:42 2019

@author: saikats
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


def get_noise(img, mean, sigma):
    gaussian_noise = np.random.normal(mean, sigma,(img.shape))
    return gaussian_noise

def add_gaussain_noise(img,mean,sigma):
    # make a random gaussian noise
    gaussian_noise = get_noise(img, mean, sigma)
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
    
    noisy_img = add_gaussain_noise(img, 50, 32)
    gau_noise = get_noise(img,50,32)

    rows, cols = img.shape

    pixel_sum = 0
    pixel_sum_sq = 0
    
    for i in range(rows):
        for j in range(cols):
            pixel = (img[i][j] - noisy_img[i][j])
            pixel = pixel * pixel
            pixel_sum = (pixel_sum + pixel)
        
            pixel_sum_sq = pixel_sum_sq + (img[i][j]*img[i][j])


    total = rows*cols

    mse = pixel_sum/total

    snr = 20 * np.log10(pixel_sum_sq/ pixel_sum)

    psnr_tmp = (255*255)/mse

    psnr = 10 * np.log10(psnr_tmp) 

    avg_img = cv2.GaussianBlur(noisy_img,(5,5),0)
    

    cv2.normalize(avg_img, avg_img, 0, 255, cv2.NORM_MINMAX, dtype=-1)
    avg_img = avg_img.astype(np.uint8)


    pixel_sum = 0
    pixel_sum_sq = 0

    for i in range(rows):
        for j in range(cols):
            pixel = (noisy_img[i][j] - avg_img[i][j])
            pixel = (pixel * pixel)
            pixel_sum = (pixel_sum + pixel)
        
            pixel_sum_sq = pixel_sum_sq + (noisy_img[i][j]*noisy_img[i][j])


    total = rows*cols

    a_mse = pixel_sum/total

    a_snr = pixel_sum_sq/ pixel_sum

    psnr_tmp = (255*255)/a_mse

    a_psnr = 10 * np.log10(psnr_tmp) 





    fig = plt.figure(figsize=(10,4))
    fig.add_subplot(1,4,1)
    plt.title("Original Image")
    plt.axis('off')
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')

    fig.add_subplot(1,4,2)
    plt.title("Gaussian Noise")
    plt.axis('off')
    plt.imshow(gau_noise, cmap = 'gray', interpolation = 'bicubic')
    
    fig.add_subplot(1,4,3)
    plt.title("Noisy Image")
    plt.axis('off')
    plt.imshow(noisy_img, cmap = 'gray', interpolation = 'bicubic')

    fig.add_subplot(1,4,4)
    plt.title("Gaussain Filtering")
    plt.axis('off')
    plt.imshow(avg_img, cmap = 'gray', interpolation = 'bicubic')
    
    print('With Noisy Image:')
    print('MSE : ', mse)
    print('SNR : ', snr)
    print('PSNR : ', psnr)
    print('\n')
    print('With Average Filter Image:')
    print('MSE : ', a_mse)
    print('SNR : ', a_snr)
    print('PSNR : ', a_psnr)
    