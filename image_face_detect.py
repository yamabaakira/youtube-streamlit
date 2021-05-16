# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 21:57:09 2021

@author: akira
"""
import streamlit as st
import cv2 as cv
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

st.title('顔検出アプリ')

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img_path = f'img/{uploaded_file.name}'
    img.save(img_path)
    st.image(img)
    




    # print(len(faces))

    # for (x, y, w, h) in faces:
    #     cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) #顔認識部分を青色で囲う
    #     eye_gray = gray[y:y+h, x:x+w] #顔部分をグレー化
    #     eye_color = img[y:y+h, x:x+w] #顔部分を取り出し
    #     eyes = eye_cascade.detectMultiScale(eye_gray)
    #     print(len(eyes))
        
    #     for (ex, ey, ew, eh) in eyes:
    #         cv.rectangle(eye_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2) #目認識部分を緑色で囲う

    # cv.imshow('img', img)
    # cv.imwrite('abcd.jpg', img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()


