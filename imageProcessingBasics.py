import cv2

img=cv2.imread('Samples/flower.jpg')    #read the image from image location

img[200][200]=[255,255,255]     #changed pixels color

img[200:210, 200:210]=[0,0,0]

cv2.rectangle(img,(40,40),(140,140),(0,255,0),1)    #draw a rectangle
#syntax---> cv2.rectangle("image","start point","ending point","width","rectangleline size")

cv2.putText(img,'RECTANGLE1',(40,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,225,255),2)
#syntax --> cv2.putText("image","typed name","initial place","font name","font size","font color","font thickness")

cv2.imshow('FLOWER',img)        #show image

