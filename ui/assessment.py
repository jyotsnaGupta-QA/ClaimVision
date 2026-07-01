import streamlit as st
import pandas as pd
from services.assessment_service import AssessmentService


def show_assessment():

    st.title("🤖 AI Vehicle Damage Assessment")

    image_path = st.session_state.get("image_path")

    if not image_path:

        st.error("No uploaded image found.")

        if st.button(
            "⬅ Back to Upload",
            use_container_width=True,
        ):
            st.session_state["page"] = "image_upload"
            st.rerun()

        service = AssessmentService()
        result = service.assess(image_path)

        st.success("✅ AI Assessment Completed")

        st.divider()

        st.subheader("Vehicle Images")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Original Image")

            st.image(
                image_path,
                use_container_width=True,
            )

        with col2:
            st.markdown("### AI Processed Image")

            st.image(
                result.processed_image,
                channels="BGR",
                use_container_width=True,
            )

        st.subheader("Assessment Summary")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Damage Regions",
                len(result.damages)
            )

            st.metric(
                "Estimated Cost",
                f"₹{result.total_cost:,}"
            )

        with col2:
            st.metric(
                "Fraud Score",
                result.fraud["fraud_score"]
            )

            st.metric(
                "Risk Level",
                result.fraud["risk_level"]
            )

        st.divider()
        st.subheader("Detected Damage Regions")

        if result.damages:

            damage_rows = []

            for damage in result.damages:

                damage_rows.append(
                    {
                        "Damage ID": damage["damage_id"],
                        "Severity": damage["severity"],
                        "Area": round(damage["area"], 2),
                        "Width": damage["width"],
                        "Height": damage["height"],
                    }
                )

            df = pd.DataFrame(damage_rows)

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
            )

        else:
            st.info("No significant damage detected.")

        st.divider()
        st.subheader("AI Recommendation")

        fraud_score = result.fraud["fraud_score"]

        if fraud_score < 30:
            st.success("🟢 Recommendation: APPROVE CLAIM")

        elif fraud_score < 70:
            st.warning("🟡 Recommendation: MANUAL REVIEW")

        else:
            st.error("🔴 Recommendation: HIGH FRAUD RISK")

        st.divider()

    if st.button(
        "⬅ Back to Upload",
        use_container_width=True,
    ):
        st.session_state["page"] = "image_upload"
        st.rerun()