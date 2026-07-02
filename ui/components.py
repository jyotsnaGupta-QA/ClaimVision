import streamlit as st


def metric_card(title, value):

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section(title):

    st.markdown(
        f"""
        <div class="card">
            <h3>{title}</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )


def status_badge(text, color):

    st.markdown(
        f"""
        <span style="
        background:{color};
        color:white;
        padding:6px 14px;
        border-radius:20px;
        font-size:13px;
        ">
        {text}
        </span>
        """,
        unsafe_allow_html=True,
    )