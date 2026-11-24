import streamlit as st

st.title("Hello World! 👋")
st.write("Streamlit Community Cloud 첫 배포 예제입니다.")

name = st.text_input("이름을 입력하세요:")
if st.button("인사하기"):
    st.success(f"안녕하세요, {name or '방문자'}님! 배포에 성공했습니다.")