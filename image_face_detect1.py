# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 21:57:09 2021

@author: akira
"""

import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

img = cv.imread('DSC_0254.JPG')

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY) #写真をグレー化
faces = face_cascade.detectMultiScale(gray, 1.3, 5) #顔認識人数分

print(len(faces))

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) #顔認識部分を青色で囲う
    eye_gray = gray[y:y+h, x:x+w] #顔部分をグレー化
    eye_color = img[y:y+h, x:x+w] #顔部分を取り出し
    # eyes = eye_cascade.detectMultiScale(eye_gray)
    # print(len(eyes))
    
    # for (ex, ey, ew, eh) in eyes:
    #     cv.rectangle(eye_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2) #目認識部分を緑色で囲う

#cv.imshow('img', img)
cv.imwrite('abcde.jpg', img)
cv.waitKey(0)
cv.destroyAllWindows()


