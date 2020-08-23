import cv2
import face
import os
import faceRecognition as fr
import numpy as np
test_img=cv2.imread('images/2.png')
faces_detected,gray_img=fr.faceDetection(test_img)
print("faces detected: ",faces_detected)
for(x,y,w,h) in faces_detected:
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,225,0),2)
resized_img=cv2.resized_img(test_img,(1000,700))
cv2.imshow("Face",resized_img)
cv2.waitKey(4000)
cv2.destroyAllWindows()
