import streamlit as st
import random
import sympy


st.title("素因数分解")
if st.button("スタート"):
    x = random.randrange(1,139,1)
    y = random.randrange(1,17,1)

    if 0 < x <= 10:
         st.write("次の数を素因数分解してください")
         st.write(x * y * 3)
    
    else:
         st.write("次の数を素因数分解してください")
         st.write(x * 13 + y)


else:
    st.write("ボタンを押してください")
  

if st.button("解答"):
    
    if 0 < x <= 10:
        st.write(sympy.factorint(x * y * 3))

    else:
        st.write(sympy.factorint(x * 13 + y))

else:

    st.write("解答はこちらです")