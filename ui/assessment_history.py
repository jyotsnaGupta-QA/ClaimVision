import streamlit as st
import pandas as pd

from database.repository import ClaimRepository
from ui.theme import page_header
from ui.components import metric_card


def show_assessment_history():
    page_header(
        "📊 Assessment History",
        "Review all AI-generated vehicle damage assessments."
    )

    repo = ClaimRepository()

    try:
        history = repo.get_all_damage_assessments()

        # ==========================================================
        # NO DATA
        # ==========================================================

        if not history:
            st.info("No assessment history found.")
            return

        # ==========================================================
        # SUMMARY CARDS
        # ==========================================================

        total_assessments = len(history)

        high_risk = sum(
            1
            for item in history
            if float(item.FraudScore) >= 70
        )

        average_cost = (
            sum(float(item.EstimatedCost) for item in history)
            / total_assessments
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            metric_card(
                "Total Assessments",
                total_assessments,
            )

        with col2:
            metric_card(
                "High Risk Cases",
                high_risk,
            )

        with col3:
            metric_card(
                "Average Cost",
                f"₹{average_cost:,.0f}",
            )

        st.divider()

        # ==========================================================
        # SEARCH & FILTER
        # ==========================================================

        col1, col2 = st.columns(2)

        with col1:
            search = st.text_input(
                "🔍 Search Claim ID",
                placeholder="Enter Claim ID..."
            )

        with col2:
            severity_filter = st.selectbox(
                "Severity",
                [
                    "All",
                    "Low",
                    "Medium",
                    "High",
                ]
            )

        rows = []

        for item in history:

            if (
                search
                and search.lower()
                not in str(item.ClaimId).lower()
            ):
                continue

            if (
                severity_filter != "All"
                and item.Severity != severity_filter
            ):
                continue

            rows.append(
                {
                    "Assessment ID": item.AssessmentId,
                    "Claim ID": item.ClaimId,
                    "Severity": item.Severity,
                    "Estimated Cost (₹)": item.EstimatedCost,
                    "Fraud Score": item.FraudScore,
                    "Recommendation": item.Recommendation,
                    "Confidence": item.Confidence,
                    "Created": item.CreatedDate,
                }
            )

        df = pd.DataFrame(rows)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
        )

    except Exception as ex:
        st.error(f"Unable to load assessment history.\n\n{ex}")

    finally:
        repo.close()

    st.divider()

    col1, col2 = st.columns([1, 5])

    with col1:

        if st.button(
            "🏠 Dashboard",
            use_container_width=True,
        ):
            st.session_state["page"] = "dashboard"
            st.rerun()

    with col2:
        st.caption(
            "🚗 ClaimVision v1.0 | AI-Powered Vehicle Damage Assessment & Claim Intelligence"
        )

