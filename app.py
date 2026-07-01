import streamlit as st

from ui.dashboard import show_dashboard
from ui.claim_form import show_claim_form
from ui.image_upload import show_image_upload
from ui.assessment import show_assessment
from ui.assessment_history import show_assessment_history


st.set_page_config(
    page_title="ClaimVision",
    page_icon="🚗",
    layout="wide"
)

# Initialize navigation
if "page" not in st.session_state:
    st.session_state["page"] = "dashboard"

# Route pages
if st.session_state["page"] == "dashboard":
    show_dashboard()

elif st.session_state["page"] == "claim_form":
    show_claim_form()

elif st.session_state["page"] == "image_upload":
    show_image_upload()

elif st.session_state["page"] == "assessment":
    show_assessment()

elif st.session_state["page"] == "assessment_history":
    show_assessment_history()
