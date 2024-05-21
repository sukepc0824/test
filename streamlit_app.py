import streamlit as st
add_selectbox = st.sidebar.selectbox(
    "何をプレイする？",
    ("因数分解", "公式クイズ", )
)

st.title("因数分解")
st.text("好きな数字を選んでください")

number = st.slider("スライダー",min_value=0, max_value=100)

st.button("ここをタップ")
if st.button("ここをタップ"):
    st.write(number + number % 6 + number / 3)
else:
    st.write("数字を選んでください")
""" 
https://docs.streamlit.io/develop/api-reference
↑困ったらこれを見よう！！

//アイデア
全部作ろう！！！！
・因数分解（割と簡単）
    ランダムな数a,b,c,dを生成
    2*a+3*b+5*c+7*d=素数ではない数を生成
    
・公式クイズ（割と複雑）←おみくじ
"""