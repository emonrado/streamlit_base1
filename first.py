import streamlit as st
st.title("Hello World !")
st.text('Fixed width text')
st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size', ['S', 'M', 'L'])
st.date_input('Your birthday')
st.download_button('Download file', data)
st.camera_input("Take a picture")
st.color_picker('Pick a color')
