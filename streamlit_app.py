import streamlit as st
import random

difficulty = 3
prime_lists = [2,3,5,7]

@st.experimental_dialog("Game Over!")
def gameover():
    if st.button("リプレイ"):
        st.rerun()

def generate_product(multiply_number):
    return random.randint(1,difficulty)*multiply_number

def devide(n):
    if st.session_state.number % n != 0:
        gameover()
    else:
        st.session_state.number /= n

if 'number' not in st.session_state:
    st.session_state.number = 1

    for prime in prime_lists:
        st.session_state.number *= generate_product(prime)
    

if st.button("2"):
    devide(2)

if st.button("3"):
    devide(3)

if st.button("5"):
    devide(5)

if st.button("7"):
    devide(7)

st.title(round(st.session_state.number))