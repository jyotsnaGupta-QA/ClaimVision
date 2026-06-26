import streamlit as st

from services.claim_service import ClaimService


def show_image_upload():

    st.title("📷 Upload Vehicle Damage Images")

    claim_id = st.session_state.get("claim_id")

    if not claim_id:
        st.error("No claim found. Please create a claim first.")

        if st.button("⬅ Back to Dashboard"):
            st.session_state["page"] = "dashboard"
            st.rerun()

        return

    st.info(f"Uploading images for Claim ID: {claim_id}")

    uploaded_files = st.file_uploader(
        "Select Damage Images",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    if uploaded_files:

        st.success(f"{len(uploaded_files)} image(s) selected.")

        st.subheader("Image Preview")

        for image in uploaded_files:
            st.image(
                image,
                caption=image.name,
                width=300
            )

        if st.button(
            "💾 Save Images",
            use_container_width=True
        ):

            service = ClaimService()

            try:

                for uploaded_file in uploaded_files:

                    service.upload_image(
                        claim_id,
                        uploaded_file
                    )

                st.success(
                    "✅ Images uploaded successfully!"
                )

                st.balloons()

            except Exception as ex:

                st.error(f"Error: {ex}")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "⬅ Back to Dashboard",
            use_container_width=True
        ):
            st.session_state["page"] = "dashboard"
            st.rerun()

    with col2:

        if st.button(
            "📝 Create Another Claim",
            use_container_width=True
        ):
            st.session_state.pop("claim_id", None)
            st.session_state["page"] = "claim_form"
            st.rerun()