import streamlit as st

st.set_page_config(page_title="보건간호 AI 튜터", page_icon="🩺", layout="wide")

st.sidebar.title("🩺 보건간호 AI 튜터")
st.sidebar.markdown("특성화고 학생들을 위한 맞춤형 학습 도우미입니다.")
menu = st.sidebar.radio(
    "메뉴를 선택하세요:",
    ["의학용어 설명 도우미", "탐구 질문 개선 도우미"],
)

st.info("학습 화면 시안입니다. 실제 AI 응답과 자료 검색은 아직 연결되지 않았습니다.")

if menu == "의학용어 설명 도우미":
    st.title("📚 라틴어·한자 기반 의학용어 설명 도우미")
    st.markdown(
        "낯선 보건·의학 용어를 입력하면 어원과 쉬운 설명을 확인할 수 있도록 돕는 학습 도구입니다."
    )

    with st.form("term_form"):
        term = st.text_input(
            "의학·보건 용어를 검색하세요",
            placeholder="예: 족저굴곡, Tachycardia",
        )
        submitted = st.form_submit_button("용어 설명 듣기", type="primary")

    if submitted:
        if term.strip():
            st.subheader(term.strip())
            st.warning(
                "용어 사전과 검증된 교과서 자료 연결 후 어원 풀이와 쉬운 설명이 이곳에 표시됩니다."
            )
        else:
            st.warning("설명을 듣고 싶은 용어를 입력해주세요.")

elif menu == "탐구 질문 개선 도우미":
    st.title("💡 탐구 질문 개선 도우미")
    st.markdown(
        "응급상황 대처 등 문제해결학습 과정에서 떠오른 질문을 입력하고, "
        "더 깊이 있는 탐구 방향으로 발전시켜 보세요."
    )

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