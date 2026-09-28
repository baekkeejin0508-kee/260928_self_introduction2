import html

import streamlit as st

st.set_page_config(
    page_title="서울의료보건고등학교 보건교사",
    page_icon="🩺",
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap');

    :root {
        --ink: #18342f;
        --muted: #66756f;
        --green: #16745b;
        --mint: #e5f3ec;
        --coral: #e77a62;
        --paper: #f8faf6;
    }
    .stApp { background: var(--paper); color: var(--ink); }
    .block-container { max-width: 1120px; padding-top: 2rem; padding-bottom: 4rem; }
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stSidebar"] { background: #edf4ef; border-right: 1px solid #d7e3dc; }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { color: var(--ink); }
    .profile-school { color: var(--muted); font-size: .88rem; line-height: 1.65; }
    .profile-role { color: var(--green); font-size: 1.1rem; font-weight: 700; }
    .profile-years { color: var(--ink); font-size: 1.5rem; font-weight: 800; }
    .eyebrow {
        color: var(--green); font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
        font-size: .78rem; font-weight: 700; letter-spacing: 0;
        text-transform: uppercase; margin-bottom: .7rem;
    }
    .hero-title {
        color: var(--ink); font-family: 'Noto Sans KR', sans-serif;
        font-size: clamp(2.25rem, 4vw, 3.6rem); font-weight: 800;
        line-height: 1.25; letter-spacing: 0; margin: 0 0 1.2rem;
    }
    .hero-title span { color: var(--green); }
    .hero-copy { color: var(--muted); font-size: 1.05rem; line-height: 1.9; }
    .school-tag {
        display: inline-block; border: 1px solid #c7d9d0; border-radius: 3px;
        color: var(--green); padding: .45rem .7rem; font-size: .82rem; font-weight: 600;
    }
    .section-kicker {
        color: var(--coral); font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
        font-size: .75rem; font-weight: 700; letter-spacing: 0; margin-bottom: .35rem;
    }
    .section-title { color: var(--ink); font-size: 1.8rem; font-weight: 800; margin: 0 0 .75rem; }
    .section-copy { color: var(--muted); line-height: 1.85; }
    .principle {
        border-top: 2px solid var(--green); padding: 1rem .15rem .25rem;
        min-height: 145px;
    }
    .principle-number { color: var(--coral); font: 700 .78rem 'DM Sans', sans-serif; }
    .principle-title { color: var(--ink); font-size: 1.12rem; font-weight: 700; margin: .45rem 0; }
    .principle-copy { color: var(--muted); font-size: .91rem; line-height: 1.7; }
    .quote-band {
        background: var(--mint); border-left: 4px solid var(--green);
        padding: 1.35rem 1.5rem; color: var(--ink); font-size: 1.08rem;
        line-height: 1.8; margin: 1.1rem 0 2.4rem;
    }
    .footer-note { color: var(--muted); font-size: .84rem; }
    div[data-testid="stImage"] img { border-radius: 4px; }
    @media (max-width: 700px) {
        .block-container { padding-top: 1rem; }
        .hero-title { font-size: 2.25rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.image(
        "https://smh.sen.hs.kr/dggb/module/file/selectImageView.do?atchFileId=1405837&fileSn=0",
        width=105,
    )
    st.markdown("### 선생님 프로필")
    teacher_name = st.text_input("이름", value="백00", placeholder="이름을 입력해 주세요")
    st.markdown('<div class="profile-years">경력 10년</div>', unsafe_allow_html=True)
    st.markdown('<div class="profile-role">보건교사</div>', unsafe_allow_html=True)
    st.markdown(
        '<p class="profile-school">서울의료보건고등학교</p>',
        unsafe_allow_html=True,
    )
    st.divider()
    st.markdown("[학교 홈페이지 방문](https://smh.sen.hs.kr/)")

st.markdown('<div class="eyebrow">Care · Health · Growth</div>', unsafe_allow_html=True)
hero_text, hero_image = st.columns([1.15, 0.85], gap="large", vertical_alignment="center")

with hero_text:
    safe_teacher_name = html.escape(teacher_name)
    greeting = f"{safe_teacher_name} 보건교사" if teacher_name else "서울의료보건고등학교 보건교사"
    st.markdown(
        f"""
        <div class="school-tag">{greeting} · 경력 10년</div>
        <h1 class="hero-title">보건의료 인재의 꿈,<br><span>건강한 학교</span>에서<br>자라납니다.</h1>
        <p class="hero-copy">
            안녕하세요. 서울의료보건고등학교에서 학생들의 건강과 안전한 학교생활을 함께 살피는 보건교사입니다.<br>
            보건의료 분야를 배우는 학생들이 몸과 마음의 건강을 지키며
            각자의 꿈을 키워가도록 곁에서 함께하겠습니다.
        </p>
        """,
        unsafe_allow_html=True,
    )

with hero_image:
    st.image(
        "https://smh.sen.hs.kr/dggb/module/image/selectDesignImageView.do?sitemapId=344775",
        caption="서울의료보건고등학교 홈페이지의 CPR 교육 이미지",
        use_container_width=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-kicker">MY PROMISE</div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">학생 곁에서, 세 가지를 지킵니다</h2>', unsafe_allow_html=True)
st.markdown(
    '<p class="section-copy">보건실은 학생들이 건강에 관한 도움을 편하게 청하고, 마음 놓고 머물 수 있는 학교 안의 공간입니다.</p>',
    unsafe_allow_html=True,
)

principles = st.columns(3, gap="large")
for column, number, title, copy in zip(
    principles,
    ("01", "02", "03"),
    ("먼저 살피겠습니다", "함께 배우겠습니다", "꾸준히 연결하겠습니다"),
    (
        "작은 몸의 신호와 마음의 변화를 놓치지 않고, 필요한 도움을 차분히 연결합니다.",
        "응급처치와 생활 속 건강 지식을 익혀 학생이 스스로 건강을 선택하도록 돕습니다.",
        "학생·가정·교직원과 소통하며 학교 안팎에서 이어지는 건강한 환경을 만듭니다.",
    ),
):
    with column:
        st.markdown(
            f'<div class="principle"><div class="principle-number">{number}</div>'
            f'<div class="principle-title">{title}</div>'
            f'<div class="principle-copy">{copy}</div></div>',
            unsafe_allow_html=True,
        )

st.markdown(
    '<div class="quote-band">“건강은 잘 해내야 하는 과제가 아니라, 서로 돌보며 배워가는 힘이라고 믿습니다.”</div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="section-kicker">AT SCHOOL</div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">학교의 하루를 건강하게</h2>', unsafe_allow_html=True)
st.markdown(
    '<p class="section-copy">학생이 안심하고 배우고 성장할 수 있도록, 일상 가까이에서 건강한 학교생활을 지원합니다.</p>',
    unsafe_allow_html=True,
)

focus_areas = st.columns(3, gap="large")
for column, title, detail in zip(
    focus_areas,
    ("응급 상황 대응", "건강한 생활 습관", "마음까지 살피는 돌봄"),
    (
        "위급한 순간 침착하게 대응하고, 학생의 안전을 우선으로 필요한 조치를 이어갑니다.",
        "감염병 예방, 바른 생활 습관, 자기 건강관리 역량을 실생활 중심으로 함께 익힙니다.",
        "몸과 마음의 어려움을 편견 없이 듣고, 상황에 맞는 교내·외 지원으로 연결합니다.",
    ),
):
    with column:
        st.markdown(f"**{title}**")
        st.markdown(f'<p class="section-copy">{detail}</p>', unsafe_allow_html=True)

st.divider()
st.markdown(
    '<p class="footer-note">서울의료보건고등학교 보건교사<br>학생의 건강한 오늘과 내일을 함께 응원합니다. '
    '<a href="https://smh.sen.hs.kr/" target="_blank">학교 홈페이지</a></p>',
    unsafe_allow_html=True,
)
