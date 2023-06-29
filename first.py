import streamlit as st
st.title("Hello World !")
st.text('固定の文字列の表示')
st.slider('スライダー形式で数字を選択できます。', 0, 100)
st.select_slider('セレクト形式で値の選択ができます。', ['S', 'M', 'L'])
st.date_input('日付の選択が可能です。')
st.camera_input("Take a picture")
st.color_picker('Pick a color')
