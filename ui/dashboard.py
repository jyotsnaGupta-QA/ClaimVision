import streamlit as st

from ui.theme import page_header
from ui.components import metric_card
from database.repository import ClaimRepository


def show_dashboard():

    st.markdown(
    """
            # 🚗 ClaimVision Dashboard

            AI-Powered Vehicle Damage Assessment & Claim Intelligence
            """
            )

    st.info(
    """
    Welcome to **ClaimVision Enterprise**.

    Use the navigation panel to create new claims, upload images,
    run AI damage assessment, and review previous assessments.
    """
    )

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
        metric_card(
            "Total Claims",
            total_claims,
        )

    with col2:
        metric_card(
            "Assessments",
            total_assessments,
        )

    with col3:
        metric_card(
            "Estimated Cost",
            f"₹{total_cost:,.0f}",
        )

    with col4:
        metric_card(
            "Avg Fraud",
            f"{avg_fraud}%",
        )

    st.markdown("<br>", unsafe_allow_html=True)

    left, right = st.columns([2.2, 1])


    # ==========================================================
    # RECENT CLAIMS
    # ==========================================================

    with left:

        st.markdown("""
        <div class='card'>
        <h3>📋 Recent Claims</h3>
        """, unsafe_allow_html=True)

        repo = ClaimRepository()

        try:
            claims = repo.get_recent_claims()
        finally:
            repo.close()

        st.dataframe(
            claims,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================================
    # RIGHT PANEL
    # ==========================================================

    with right:

        st.markdown("""
        <div class='card'>
        <h3>🤖 AI Summary</h3>
        """, unsafe_allow_html=True)

        repo = ClaimRepository()

        try:

            summary = repo.get_ai_summary()

        finally:

            repo.close()

        st.metric("High Severity", summary["high"])
        st.metric("Medium Severity", summary["medium"])
        st.metric("Low Severity", summary["low"])
        st.metric("Average Fraud Score", f'{summary["fraud"]}%')

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("")

        st.markdown("""
        <div class='card'>
        <h3>⚡ Quick Actions</h3>
        """, unsafe_allow_html=True)

        if st.button("➕ Create New Claim",
            use_container_width=True,
        ):
            st.session_state["page"] = "claim_form"
            st.rerun()

        if st.button("📷 Upload Images",
            use_container_width=True,
        ):
            st.session_state["page"] = "image_upload"
            st.rerun()

        if st.button("🤖 AI Assessment",
            use_container_width=True,
        ):
            st.session_state["page"] = "assessment"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================================
    # BOTTOM METRICS
    # ==========================================================

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("""
        <div class='card'>
        <h3>📈 Claim Status</h3>
        """, unsafe_allow_html=True)

        repo = ClaimRepository()

        try:
            status = repo.get_claim_status_summary()
        finally:
            repo.close()

        st.progress(status["completed"] / 100)

        st.write(
            f'{status["completed"]}% claims processed successfully'
        )
      
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class='card'>
        <h3>🛡 Fraud Detection</h3>
        """, unsafe_allow_html=True)
        st.progress(summary["fraud"] / 100)

        st.write(
            f'{summary["fraud"]}% claims flagged for review'
        )
        st.markdown("</div>", unsafe_allow_html=True)