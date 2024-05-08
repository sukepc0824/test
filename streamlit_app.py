import streamlit as st

st.title("BMI計算")
w = st.number_input("体重(kg)")
h = st.number_input("身長(cm)")

if st.button("計算"):
    st.write("あなたのBMIは "+str( (w/(h/100)**2)))