from pathlib import Path
import streamlit as st


def load_theme():
    """
    Load global CSS styles.
    """
    css_file = Path("assets/styles.css")

    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True,
            )


def page_header(title: str, subtitle: str):
    """
    Standard page header used across the application.
    """

    st.title(title)
    st.caption(subtitle)
    st.divider()