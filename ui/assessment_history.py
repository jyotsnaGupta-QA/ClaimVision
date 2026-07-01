import streamlit as st
import pandas as pd

from database.repository import ClaimRepository


def show_assessment_history():

    st.title("📂 Assessment History")

    repo = ClaimRepository()

    try:

        history = repo.get_all_damage_assessments()

        if not history:

            st.info(
                "No assessments available."
            )

        else:

            rows = []

            for item in history:

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

    finally:

        repo.close()

    st.divider()

    if st.button(
        "⬅ Back to Dashboard",
        use_container_width=True,
    ):

        st.session_state["page"] = "dashboard"
        st.rerun()

        st.divider()

st.caption(
    "🚗 ClaimVision v1.0 | AI-Powered Vehicle Damage Assessment | © 2026"
)