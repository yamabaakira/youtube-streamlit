import streamlit as st
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


st.title('物体検出アプリ2')

uploaded_file = st.file_uploader('Choose an image...',type = ['jpg'])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img_path = f'img/{uploaded_file.name}'
    img.save(img_path)
#    st.image(img)

    draw = ImageDraw.Draw(img)
 
    font_image = ImageFont.truetype(font='./Helvetica 400.ttf', size = 50)
    caption = 'CAR_PRIUS'
    text_w, text_h = draw.textsize(caption,font = font_image) 

    draw.rectangle([(200, 100), (3000, 2000)], fill = None, outline = 'green', width = 10)
    draw.rectangle([(200, 100), (200 + text_w, 100 + text_h)], fill = 'red')
    draw.text((200,100), caption, fill='white', font = font_image)

    st.image(img)


    st.markdown('**認識されたコンテンツタグ**')
    st.markdown(caption)
