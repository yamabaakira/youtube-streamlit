import cv2 as cv
import streamlit as st
from PIL import Image
import numpy as np
import pyocr
import os
import shutil

st.title('画面ページ認識、ファイル名自動リネーム by ymb')

HMI_type = st.selectbox(
    'select HMI:',
    ('EA9', 'CM5')
)
Object_type = st.selectbox(
    'select Object type:',
    ('Line', 'PushButton', 'Indicatorlight')
)
Sheet_type = st.selectbox(
    'select Sheet type:',
    ('Sheet1', 'Sheet2', 'Sheet3', 'Sheet4')
)

uploaded_files = st.file_uploader(
    'Choose an capture image...',
    type = ['jpg','bmp'],
    accept_multiple_files = True) #jpgファイル読込み
    
if uploaded_files is not None:
    err_count = 0
    for uploaded_file in uploaded_files:
        image=Image.open(uploaded_file)
        img = np.array(image)
        img_reshape = img[10 : 50,10 : 55]#page数を切り出し
        st.image(img_reshape)

        # OCRエンジンの取得
        tools = pyocr.get_available_tools()
        tool = tools[0]

        # OCRの実行
        img_resize = Image.fromarray(img_reshape)
        builder = pyocr.builders.DigitBuilder(tesseract_layout=6)#数値認識設定
        result = tool.image_to_string(img_resize, lang="jpn", builder=builder)#数値認識結果出力
    #    st.write('読取結果')
        if result == '':
            st.write('読取失敗')
            err_count = err_count + 1
        else:
            st.write(result)

        img_path_src = f'./{uploaded_file.name}'
        img_path_copy = f'./img/{uploaded_file.name}'
    #   shutil.copyfile(img_path_src,img_path_copy)

        img_path_rename = './'+ HMI_type + '_' + Object_type + '_' + Sheet_type + '_P' + result +'.jpg'
        print(img_path_rename)
        print(result)

        os.rename(img_path_src, img_path_rename)
    #    image.save(img_path_rename)
    
    st.write(f"""{err_count}ファイルNG/{len(uploaded_files)}ファイル""")


