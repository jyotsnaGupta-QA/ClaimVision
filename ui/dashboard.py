import streamlit as st


def show_dashboard():

    st.title("🚗 ClaimVision")
    st.caption("AI-Powered Vehicle Damage Assessment & Claim Intelligence")

    st.divider()

    # Dashboard Metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Claims", "0")

    with col2:
        st.metric("Pending", "0")

    with col3:
        st.metric("Approved", "0")

    with col4:
        st.metric("Rejected", "0")

    st.divider()

    st.subheader("Quick Actions")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📝 Start New Claim", use_container_width=True):
            st.session_state["page"] = "claim_form"
            st.rerun()

    with col2:
        st.button(
            "📂 View Claims",
            disabled=True,
            use_container_width=True
        )

    st.divider()

    st.info(
        """
        Welcome to ClaimVision.

        Current Features:
        • Create New Claim
        • Upload Vehicle Damage Images

        Upcoming Features:
        • AI Damage Detection
        • Repair Cost Estimation
        • Fraud Detection
        • Claim History
        • AI Assessment Reports
        """
    )