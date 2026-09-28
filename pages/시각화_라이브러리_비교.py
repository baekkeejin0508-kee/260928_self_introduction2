import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="시각화 라이브러리 비교",
    page_icon="📊",
    layout="wide",
)

st.markdown(
    """
    <style>
    :root {
        --ink: #18342f;
        --muted: #66756f;
        --green: #16745b;
        --mint: #e5f3ec;
        --coral: #e77a62;
        --paper: #f8faf6;
    }
    .stApp { background: var(--paper); color: var(--ink); }
    .block-container { max-width: 1200px; padding-top: 2rem; padding-bottom: 4rem; }
    .eyebrow { color: var(--coral); font-size: .78rem; font-weight: 700; }
    .intro { color: var(--muted); line-height: 1.8; }
    [data-testid="stTabs"] button { font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="eyebrow">DATA VISUALIZATION</div>', unsafe_allow_html=True)
st.title("시각화 라이브러리 비교")
st.markdown(
    '<p class="intro">같은 가상 보건교육 데이터를 Matplotlib, Seaborn, Plotly로 각각 그려보고 표현 방식과 사용 경험을 비교합니다.</p>',
    unsafe_allow_html=True,
)
st.caption("아래 숫자는 학습을 위해 만든 예시 데이터이며 실제 학교 통계가 아닙니다.")

monthly_data = pd.DataFrame(
    {
        "월": ["3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월"],
        "참여 인원(명)": [34, 42, 39, 51, 57, 55, 68, 74],
    }
)

topic_data = pd.DataFrame(
    {
        "학습 주제": ["손 위생", "응급처치", "심폐소생술", "영양과 수면", "정신건강", "감염병 예방"],
        "정답률(%)": [92, 78, 84, 86, 74, 89],
    }
)

st.markdown("### 예시 데이터 1 · 월별 보건교육 참여 인원")
with st.expander("월별 참여 데이터 보기"):
    st.dataframe(monthly_data, hide_index=True, width="stretch")

monthly_tabs = st.tabs(["Matplotlib", "Seaborn", "Plotly"])

with monthly_tabs[0]:
    figure, axis = plt.subplots(figsize=(10, 4.5))
    axis.plot(
        monthly_data["월"],
        monthly_data["참여 인원(명)"],
        color="#16745b",
        marker="o",
        linewidth=2.5,
    )
    axis.set_title("월별 보건교육 참여 인원", fontsize=16, pad=16)
    axis.set_xlabel("월")
    axis.set_ylabel("참여 인원(명)")
    axis.grid(axis="y", alpha=0.25)
    figure.tight_layout()
    st.pyplot(figure, width="stretch")
    plt.close(figure)

with monthly_tabs[1]:
    figure, axis = plt.subplots(figsize=(10, 4.5))
    sns.lineplot(
        data=monthly_data,
        x="월",
        y="참여 인원(명)",
        marker="o",
        linewidth=2.5,
        color="#e77a62",
        ax=axis,
    )
    axis.set_title("월별 보건교육 참여 인원", fontsize=16, pad=16)
    axis.set_xlabel("월")
    axis.set_ylabel("참여 인원(명)")
    axis.grid(axis="y", alpha=0.25)
    figure.tight_layout()
    st.pyplot(figure, width="stretch")
    plt.close(figure)

with monthly_tabs[2]:
    figure = px.line(
        monthly_data,
        x="월",
        y="참여 인원(명)",
        title="월별 보건교육 참여 인원",
        markers=True,
        labels={"월": "월", "참여 인원(명)": "참여 인원(명)"},
        color_discrete_sequence=["#16745b"],
    )
    figure.update_layout(font_family="Noto Sans CJK KR, sans-serif", title_x=0.02)
    st.plotly_chart(figure, width="stretch")

st.divider()
st.markdown("### 예시 데이터 2 · 학습 주제별 건강 퀴즈 정답률")
with st.expander("주제별 정답률 데이터 보기"):
    st.dataframe(topic_data, hide_index=True, width="stretch")

topic_tabs = st.tabs(["Matplotlib", "Seaborn", "Plotly"])

with topic_tabs[0]:
    figure, axis = plt.subplots(figsize=(10, 4.5))
    bars = axis.barh(
        topic_data["학습 주제"],
        topic_data["정답률(%)"],
        color="#16745b",
    )
    axis.invert_yaxis()
    axis.set_xlim(0, 100)
    axis.set_title("학습 주제별 건강 퀴즈 정답률", fontsize=16, pad=16)
    axis.set_xlabel("정답률(%)")
    axis.set_ylabel("학습 주제")
    axis.bar_label(bars, fmt="%d%%", padding=4)
    axis.grid(axis="x", alpha=0.25)
    figure.tight_layout()
    st.pyplot(figure, width="stretch")
    plt.close(figure)

with topic_tabs[1]:
    figure, axis = plt.subplots(figsize=(10, 4.5))
    sns.barplot(
        data=topic_data,
        x="정답률(%)",
        y="학습 주제",
        color="#e77a62",
        ax=axis,
    )
    axis.set_xlim(0, 100)
    axis.set_title("학습 주제별 건강 퀴즈 정답률", fontsize=16, pad=16)
    axis.set_xlabel("정답률(%)")
    axis.set_ylabel("학습 주제")
    axis.grid(axis="x", alpha=0.25)
    figure.tight_layout()
    st.pyplot(figure, width="stretch")
    plt.close(figure)

with topic_tabs[2]:
    figure = px.bar(
        topic_data,
        x="정답률(%)",
        y="학습 주제",
        orientation="h",
        title="학습 주제별 건강 퀴즈 정답률",
        labels={"정답률(%)": "정답률(%)", "학습 주제": "학습 주제"},
        color="정답률(%)",
        color_continuous_scale=["#e5f3ec", "#16745b"],
    )
    figure.update_layout(
        font_family="Noto Sans CJK KR, sans-serif",
        title_x=0.02,
        xaxis_range=[0, 100],
        yaxis={"autorange": "reversed"},
        coloraxis_showscale=False,
    )
    st.plotly_chart(figure, width="stretch")