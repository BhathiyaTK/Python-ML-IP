import cv2

camera=cv2.VideoCapture(0)  #'0' for default camera

#load face and eye detection classifier files
face_clsfr=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_clsfr=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

while(True):
    ret,img=camera.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #ret is a boolean value for confirm camera is on or not(on-true/ off-false)
    #camera.read() reads the camera and captured image set to img

    faces=face_clsfr.detectMultiScale(gray) #detect face scale

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        #draw a rectangle on detected face
        cv2.putText(img,'FACE DETECTED',(40,40),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,225,255),1)
                   
    cv2.imshow('LIVE',img)  #captured img shows
    cv2.waitKey(10)     #add delay to show captured image frames(10milisecond)
