import streamlit as st 
counter = 0
button = st.button("클릭~!!")

if button:
    counter = couter + 1
    
st.write(counter)
