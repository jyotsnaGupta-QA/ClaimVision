import streamlit as st


PAGES = {
    "🏠 Dashboard": "dashboard",
    "📝 New Claim": "claim_form",
    "📷 Upload Images": "image_upload",
    "🤖 AI Assessment": "assessment",
    "📊 Assessment History": "assessment_history",
}

REVERSE_PAGES = {v: k for k, v in PAGES.items()}


def show_sidebar():

    if "page" not in st.session_state:
        st.session_state["page"] = "dashboard"

    with st.sidebar:

        st.markdown("## 🚗 ClaimVision")
        st.caption("AI Vehicle Damage Assessment")

        labels = list(PAGES.keys())

        current_label = REVERSE_PAGES.get(
            st.session_state["page"],
            "🏠 Dashboard",
        )

        selected = st.radio(
            "Navigation",
            labels,
            index=labels.index(current_label),
        )

        st.session_state["page"] = PAGES[selected]

    return st.session_state["page"]