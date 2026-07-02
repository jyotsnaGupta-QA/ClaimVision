import streamlit as st


def show_header(title: str, subtitle: str):

    st.markdown(
        f"""
        <div style="
            background:linear-gradient(90deg,#2563EB,#1D4ED8);
            padding:25px;
            border-radius:15px;
            color:white;
            margin-bottom:25px;
        ">

        <h1 style="margin-bottom:0;">
            {title}
        </h1>

        <p style="margin-top:8px;font-size:16px;">
            {subtitle}
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )