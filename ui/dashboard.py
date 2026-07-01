import streamlit as st
from database.repository import ClaimRepository


def show_dashboard():

    st.title("🚗 ClaimVision")
    st.caption("AI-Powered Vehicle Damage Assessment & Claim Intelligence")

    st.divider()

    repo = ClaimRepository()

    try:

        total_claims = repo.get_total_claims()
        total_assessments = repo.get_total_assessments()
        total_cost = repo.get_total_estimated_cost()
        avg_fraud = repo.get_average_fraud_score()

    finally:

        repo.close()


    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Claims",
            total_claims,
        )

    with col2:
        st.metric(
            "Assessments",
            total_assessments,
        )

    with col3:
        st.metric(
            "Estimated Cost",
            f"₹{total_cost:,.0f}",
        )

    with col4:
        st.metric(
            "Avg Fraud Score",
            avg_fraud,
        )

    st.divider()

    st.subheader("Quick Actions")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📝 Start New Claim", use_container_width=True):
            st.session_state["page"] = "claim_form"
            st.rerun()

    with col2:
       if st.button(
        "📂 Assessment History",
        use_container_width=True,
    ):
        st.session_state["page"] = "assessment_history"
        st.rerun()

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