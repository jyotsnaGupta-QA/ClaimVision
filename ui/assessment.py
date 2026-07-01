import streamlit as st
import pandas as pd

from services.assessment_service import AssessmentService
from services.report_service import ReportService


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

        return

    service = AssessmentService()

    try:

        # ----------------------------
        # Run AI Assessment
        # ----------------------------

        result = service.assess(image_path)

        claim_id = st.session_state.get("claim_id")

        # ----------------------------
        # Save Assessment Once
        # ----------------------------

        if "assessment_saved" not in st.session_state:
            st.session_state["assessment_saved"] = False

        if not st.session_state["assessment_saved"]:

            service.save_assessment(
                claim_id=claim_id,
                result=result,
            )

            st.session_state["assessment_saved"] = True

        # ----------------------------
        # Success
        # ----------------------------

        st.success("✅ AI Assessment Completed")

        # ----------------------------
        # Images
        # ----------------------------

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

        # ----------------------------
        # Summary
        # ----------------------------

        st.divider()

        st.subheader("Assessment Summary")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "Damage Regions",
                len(result.damages),
            )

        with c2:
            st.metric(
                "Estimated Cost",
                f"₹{result.total_cost:,.0f}",
            )

        with c3:
            st.metric(
                "Fraud Score",
                result.fraud["fraud_score"],
            )

        with c4:
            st.metric(
                "Risk Level",
                result.fraud["risk_level"],
            )

        # ----------------------------
        # Damage Table
        # ----------------------------

        st.divider()

        st.subheader("Detected Damage Regions")

        if result.damages:

            rows = []

            for damage in result.damages:

                rows.append(
                    {
                        "Damage ID": damage["damage_id"],
                        "Severity": damage["severity"],
                        "Area": round(
                            damage["area"],
                            2,
                        ),
                        "Width": damage["width"],
                        "Height": damage["height"],
                    }
                )

            df = pd.DataFrame(rows)

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
            )

        else:

            st.info(
                "No significant damage detected."
            )

        # ----------------------------
        # Recommendation
        # ----------------------------

        st.divider()

        st.subheader("AI Recommendation")

        fraud_score = result.fraud["fraud_score"]

        if fraud_score < 30:

            st.success(
                "🟢 Recommendation: APPROVE CLAIM"
            )

        elif fraud_score < 70:

            st.warning(
                "🟡 Recommendation: MANUAL REVIEW"
            )

        else:

            st.error(
                "🔴 Recommendation: HIGH FRAUD RISK"
            )

    except Exception as ex:

        st.error(f"Error: {ex}")

    # ----------------------------
    # Navigation
    # ----------------------------

    st.divider()

    report = ReportService()

    pdf_file = f"Assessment_{claim_id}.pdf"

    if st.button(
        "📄 Generate PDF Report",
        use_container_width=True,
    ):

        report.generate_report(
            pdf_file,
            claim_id,
            result,
        )

        with open(pdf_file, "rb") as f:

            st.download_button(
                "⬇ Download Report",
                data=f,
                file_name=pdf_file,
                mime="application/pdf",
            )

    if st.button(
        "⬅ Back to Upload",
        use_container_width=True,
    ):

        st.session_state.pop(
            "assessment_saved",
            None,
        )

        st.session_state["page"] = "image_upload"

        st.rerun()

        st.divider()

        st.caption(
            "🚗 ClaimVision v1.0 | AI-Powered Vehicle Damage Assessment | © 2026"
)