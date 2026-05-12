import streamlit as st
from datetime import datetime

st.title("실습 3 - Streamlit 앱 EC2 배포")
st.caption("오픈소스소프트웨어실습 실습 3 - Streamlit 앱 EC2 배포")

st.subheader("텍스트 분석기")
user_input = st.text_input("텍스트를 입력하세요", placeholder="여기에 입력하세요...")

if st.button("변환하기", key="text_btn"):
    if user_input.strip():
        print(f"[{datetime.now()}] 버튼 클릭 - 입력값: '{user_input}' | 글자 수: {len(user_input)}, 단어 수:{len(user_input.split())}")
        st.success(f"입력한 텍스트: **{user_input}**")
        st.info(f"글자 수: {len(user_input)}자 / 단어 수: {len(user_input.split())}개")
    else:
        print(f"[{datetime.now()}] 버튼 클릭 - 입력값 없음")
        st.warning("텍스트를 입력해주세요.") 

st.divider()