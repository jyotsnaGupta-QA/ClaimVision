import streamlit as st

from services.claim_service import ClaimService


def show_image_upload():
    """
    Vehicle image upload screen.
    """

    st.title("📷 Upload Vehicle Damage Images")

    claim_id = st.session_state.get("claim_id")

    if not claim_id:
        st.error("No claim found. Please create a claim first.")

        if st.button("⬅ Back to Dashboard"):
            st.session_state["page"] = "dashboard"
            st.rerun()

        return

    # Initialize session state
    if "image_saved" not in st.session_state:
        st.session_state["image_saved"] = False

    st.info(f"Uploading images for Claim ID: {claim_id}")

    uploaded_files = st.file_uploader(
        "Select Damage Images",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
    )

    if uploaded_files:

        st.success(f"{len(uploaded_files)} image(s) selected.")

        st.subheader("Image Preview")

        for image in uploaded_files:
            st.image(
                image,
                caption=image.name,
                width=350,
            )

        # -----------------------------
        # Save Images
        # -----------------------------
        if not st.session_state["image_saved"]:

            if st.button(
                "💾 Save Images",
                use_container_width=True,
            ):

                service = ClaimService()

                try:

                    last_saved_path = None

                    for uploaded_file in uploaded_files:

                        last_saved_path = service.upload_image(
                            claim_id,
                            uploaded_file,
                        )

                    st.session_state["image_path"] = last_saved_path
                    st.session_state["image_saved"] = True

                    st.success("✅ Images uploaded successfully!")

                    st.balloons()

                    st.rerun()

                except Exception as ex:

                    st.error(f"Error uploading images: {ex}")

        # -----------------------------
        # Run AI Assessment
        # -----------------------------
        if st.session_state["image_saved"]:

            st.success("✅ Images uploaded successfully!")

            if st.button(
                "🤖 Run AI Assessment",
                use_container_width=True,
            ):

                st.session_state["page"] = "assessment"
                st.rerun()

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "⬅ Back to Dashboard",
            use_container_width=True,
        ):

            st.session_state.pop("assessment_saved", None)
            st.session_state.pop("image_saved", None)
            st.session_state["page"] = "dashboard"
            st.rerun()

    with col2:

        if st.button(
            "📝 Create Another Claim",
            use_container_width=True,
        ):

            st.session_state.pop("claim_id", None)
            st.session_state.pop("image_saved", None)
            st.session_state.pop("image_path", None)

            st.session_state["page"] = "claim_form"
            st.rerun()

            st.divider()

            st.caption(
                "🚗 ClaimVision v1.0 | AI-Powered Vehicle Damage Assessment | © 2026"
)