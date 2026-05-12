import streamlit as st
import datetime

# 페이지 기본 설정
st.set_page_config(page_title="EC2실습")
st.title("실습 3 - Streamlit 앱 EC2 배포")
st.caption("오픈소스소프트웨어실습 실습 3 - Streamlit 앱 EC2 배포")

st.subheader("텍스트 분석기")
user_input = st.text_input("텍스트를 입력하세요", placeholder="여기에 입력하세요...")

if st.button("변환하기", key="text_btn"):
    if user_input.strip():
        col1, col2 = st.columns(2)
        with col1:
            st.success(f"입력한 텍스트: **{user_input}**")
        with col2:
            st.info(f"글자 수: {len(user_input)}자 / 단어 수: {len(user_input.split())}개")
    else:
        st.warning("텍스트를 입력해주세요.")

st.divider()