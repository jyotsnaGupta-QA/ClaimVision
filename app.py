import streamlit as st

from ui.dashboard import show_dashboard
from ui.claim_form import show_claim_form
from ui.image_upload import show_image_upload
from ui.assessment import show_assessment
from ui.assessment_history import show_assessment_history
from ui.sidebar import show_sidebar
from ui.theme import load_theme


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="ClaimVision",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------------------------------
# Load Global Theme
# -------------------------------------------------

load_theme()

# -------------------------------------------------
# Sidebar Navigation
# -------------------------------------------------

page = show_sidebar()

if page == "dashboard":
    show_dashboard()

elif page == "claim_form":
    show_claim_form()

elif page == "image_upload":
    show_image_upload()

elif page == "assessment":
    show_assessment()

elif page == "assessment_history":
    show_assessment_history()