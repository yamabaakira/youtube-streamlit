import cv2 as cv
import streamlit as st
from PIL import Image
import numpy as np


st.title('人検出アプリ　opencv/streamlit by ymb')
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml') #顔認識分類器を読み込み
body_cascade = cv.CascadeClassifier('haarcascade_fullbody.xml') #体認識分類器を読み込み
smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml') #笑顔認識分類器を読み込み

uploaded_file = st.file_uploader('Choose an image...',type = ['jpg']) #jpgファイル読込み

#分類器の選択　顔認識 or 体認識の選択
option = st.selectbox(
    'select detction parts:',
    ('face', 'body')
)

#顔認識の場合には笑顔チェックの選択も可能
if option == 'face':
    smile_ckeck = st.checkbox('smile check')
    smile_count = 0

#認識範囲の選択
range = st.slider(
    'select detction range',
     min_value=0, max_value=300, step=10, value=20
)

#jpgファイル読込みデータ有
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    img = np.array(image)

    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY) #写真をグレー化

    if option == 'face':
        detections = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(range, range)) #人数分
    elif option == 'body':
        detections = body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(range, range)) #人数分

    for (x, y, w, h) in detections:
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) 

        if smile_ckeck == True:    #笑顔チェックあり
            smile_gray = gray[y:y+h, x:x+w] #顔部分をグレー化
            smile_color = img[y:y+h, x:x+w] #顔部分を取り出し
            smiles = smile_cascade.detectMultiScale(smile_gray, scaleFactor=1.1, minNeighbors=3, minSize=(range, range)) #人数笑顔チェック
            smile_count = smile_count + len(smiles)
            for (ex, ey, ew, eh) in smiles:
                cv.rectangle(smile_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2) #スマイル認識部分を緑色で囲う    


    st.write('検出後画像')
    st.write(f"""{option}検出人数：{len(detections)}人検出""")
    if smile_ckeck == True:
        st.write(f"""笑顔検出人数：{smile_count}人検出""")
    st.image(img)
  

   




