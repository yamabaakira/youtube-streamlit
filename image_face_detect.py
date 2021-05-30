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

uploaded_file = st.file_uploader('Choose an image...',type = ['jpg'])

if uploaded_file is not None:
#    img = Image.open(uploaded_file)
#    img_path = f'img/{uploaded_file.name}'
#    img.save(img_path)
#    img = ImageDraw.Draw(img)

    img = cv.imread('DSC_0254.JPG')
    st.write('元画像')
    st.image(img)

    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY) #写真をグレー化
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #顔認識人数分

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) #顔認識部分を青色で囲う
        eye_gray = gray[y:y+h, x:x+w] #顔部分をグレー化
        eye_color = img[y:y+h, x:x+w] #顔部分を取り出し

    print(len(faces))
    st.write('検出後画像')
    st.write(f"""顔検出人数：{len(faces)}人検出""")

    st.image(img)




