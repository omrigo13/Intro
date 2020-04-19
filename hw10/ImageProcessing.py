# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 21:13:03 2019

@author: omrig
"""

def inverse_img(img):
    new = img.copy()
    num = lambda p: 255 - p
    return num(new)

def merge_images(image1, image2):
    return inverse_img(inverse_img(image1) + inverse_img(image2))

def generate_encryption_key(img):
    new = img.copy()
    num = lambda p: -p
    return num(new)

def encrypt(img, key):
    new = img.copy()
    num = lambda p: p + key
    return num(new)
    
def decrypt(img, key):
    new = img.copy()
    num = lambda p: p - key
    return num(new)