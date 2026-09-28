import streamlit as st

st.set_page_config(page_title="탐구 질문 개선 도우미", page_icon="💡", layout="wide")

st.sidebar.title("🩺 보건간호 AI 튜터")
st.sidebar.markdown("특성화고 학생들을 위한 탐구 학습 도우미입니다.")

st.title("💡 탐구 질문 개선 도우미")
st.markdown(
    "응급상황 대처 등 문제해결학습 과정에서 떠오른 질문을 입력하고, "
    "더 깊이 있는 탐구 방향으로 발전시켜 보세요."
)
st.info("학습 화면 시안입니다. 실제 AI 질문 분석 기능은 아직 연결되지 않았습니다.")

with st.form("question_form"):
    question = st.text_area(
        "학생 탐구 질문 초안을 입력하세요",
        placeholder="예: 심폐소생술에서 가슴 압박의 깊이가 중요한 이유는 무엇일까?",
        height=150,
    )
    submitted = st.form_submit_button("질문 개선 피드백 받기", type="primary")

if submitted:
    if question.strip():
        st.subheader("입력한 질문")
        st.write(question.strip())
        st.warning(
            "질문 분석과 맞춤형 피드백 기능이 연결되면 탐구 방향과 개선 질문이 이곳에 표시됩니다."
        )
    else:
        st.warning("탐구 질문 초안을 입력해주세요.")