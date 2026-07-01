import streamlit as st
from datetime import datetime

from services.claim_service import ClaimService


def show_claim_form():

    st.title("📝 New Insurance Claim")

    with st.form("claim_form"):

        st.subheader("👤 Customer Information")

        customer_name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")

        st.divider()

        st.subheader("🚘 Vehicle Information")

        vehicle_number = st.text_input("Vehicle Number")
        vehicle_brand = st.text_input("Vehicle Brand")
        vehicle_model = st.text_input("Vehicle Model")

        vehicle_year = st.number_input(
            "Manufacturing Year",
            min_value=1990,
            max_value=2035,
            value=2023
        )

        policy_number = st.text_input("Insurance Policy Number")

        st.divider()

        st.subheader("🚧 Accident Information")

        accident_date = st.date_input("Accident Date")

        accident_location = st.text_input("Accident Location")

        description = st.text_area(
            "Accident Description",
            height=120
        )

        submitted = st.form_submit_button(
            "Submit Claim",
            use_container_width=True
        )

    if submitted:

        if (
            not customer_name
            or not vehicle_number
            or not accident_location
        ):
            st.error("Please fill all mandatory fields.")
            return

        service = ClaimService()

        try:

            claim = service.create_claim(
                customer_name,
                email,
                phone,
                vehicle_number,
                vehicle_brand,
                vehicle_model,
                vehicle_year,
                policy_number,
                datetime.combine(
                    accident_date,
                    datetime.min.time()
                ),
                accident_location,
                description
            )

            # Store Claim ID
            st.session_state["claim_id"] = claim.ClaimId

            st.success(
                f"✅ Claim #{claim.ClaimId} created successfully!"
            )

            st.balloons()

            # Navigate to Image Upload
            st.session_state["page"] = "image_upload"

            st.rerun()

        except Exception as ex:

            st.error(f"Error: {ex}")

    st.divider()

    if st.button("⬅ Back to Dashboard"):

        st.session_state["page"] = "dashboard"

        st.rerun()

        st.divider()

        st.caption(
            "🚗 ClaimVision v1.0 | AI-Powered Vehicle Damage Assessment | © 2026"
)