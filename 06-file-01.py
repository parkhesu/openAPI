import streamlit as st  

uploaded_file = st.file_uploader("파일을 업로드하세요")
if uploaded_file:
    st.write(uploaded_file.name)
    file_content = uploaded_file.read().decode("utf-8")
    st.write(file_content)