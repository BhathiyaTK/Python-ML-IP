import cv2

camera=cv2.VideoCapture(0)  #'0' for default camera
while(True):
    ret,img=camera.read()
    #ret is a boolean value for confirm camera is on or not(on-true/ off-false)
    #camera.read() reads the camera and captured image set to img 

    cv2.imshow('LIVE',img)  #captured img shows
    cv2.waitKey(10)     #add delay to show captured image frames(10milisecond)
