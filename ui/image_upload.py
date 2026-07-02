import streamlit as st
from PIL import Image
from services.claim_service import ClaimService
from services.assessment_service import AssessmentService

from ui.theme import page_header


def show_image_upload():

    page_header(
        "📷 Upload Vehicle Images",
        "Upload clear vehicle damage images for AI assessment."
    )

    st.info(
    """
    Upload **clear images** of the damaged vehicle.

    ### Supported Formats
    - JPG
    - JPEG
    - PNG

    ### Tips for Best Results
    - Capture the full damaged area.
    - Ensure good lighting.
    - Avoid blurry images.
    - Upload multiple angles if available.
    """
    )

    st.markdown("""
    <div class="card">
        <h3>Upload Images</h3>
        <p>You can upload multiple JPG, JPEG or PNG images.</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded_files = st.file_uploader(
        "Choose Vehicle Images",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )

    if not uploaded_files:
        st.info("Upload one or more vehicle images to continue.")
        return

    st.markdown("### 🖼 Image Preview")

    cols = st.columns(3)

    for index, uploaded_file in enumerate(uploaded_files):

        with cols[index % 3]:

            image = Image.open(uploaded_file)

            st.image(
                image,
                use_container_width=True
            )

            st.markdown(
                f"""
                <div class="card">
                    <b>{uploaded_file.name}</b><br>
                    Size: {round(uploaded_file.size/1024,2)} KB
                </div>
                """,
                unsafe_allow_html=True
            )

    st.divider()

    left, middle, right = st.columns([2, 2, 6])

    with left:

        save_clicked = st.button(
            "💾 Save Images",
            use_container_width=True
        )

    with middle:

        assess_clicked = st.button(
            "🤖 Run AI Assessment",
            use_container_width=True
        )

    if save_clicked:

        if "claim_id" not in st.session_state:

            st.error("Please create a claim first.")

        else:

            service = ClaimService()

            claim_id = st.session_state["claim_id"]

            for uploaded_file in uploaded_files:

                service.upload_image(
                    claim_id,
                    uploaded_file,
                )

            st.success("✅ Images uploaded successfully.")

    if assess_clicked:

        if "claim_id" not in st.session_state:

            st.error("Please create a claim first.")

        else:

            claim_service = ClaimService()

            assessment_service = AssessmentService()

            claim_id = st.session_state["claim_id"]

            progress = st.progress(0)

            status = st.empty()

            image_paths = []

            for file in uploaded_files:

                status.info(f"Uploading {file.name}...")

                image_path = claim_service.upload_image(
                    claim_id,
                    file,
                )

                image_paths.append(image_path)

            if not image_paths:

                st.error("No images uploaded.")

            else:

                status.info("Running AI Assessment...")

                progress.progress(30)

                result = assessment_service.assess(
                    image_paths[0]
                )

                progress.progress(75)

                assessment_service.save_assessment(
                    claim_id,
                    result,
                    processed_image_path=None,
                )

                progress.progress(100)

                st.session_state["assessment_result"] = result

                status.success(
                    "Assessment Completed Successfully."
                )

                st.success(
                    "✅ Assessment saved successfully."
                )

                st.session_state["page"] = "assessment"

                st.rerun()