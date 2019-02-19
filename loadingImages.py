import cv2

img=cv2.imread('<image path here>/image name with its extension>')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

(height,width)=gray.shape       #image dimentions
#print(height,width)

import random

for i in range(100):
    r=random.randint(0,height-1)    #randomly select height pixels
    c=random.randint(0,width-1)     #randomly select width pixels
    gray[r][c]=255      #add white color

blur=cv2.blur(gray,(7,7))   #Noise removal
ret,bw=cv2.threshold(blur,100,255,cv2.THRESH_BINARY) #ret is return value(true or false)

cv2.imshow('Color image',img)
cv2.imshow('Gray image',gray)
cv2.imshow('Blur image',blur)
cv2.imshow('Treshold image',bw)
