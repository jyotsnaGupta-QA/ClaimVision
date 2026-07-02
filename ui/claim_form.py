import streamlit as st

from ui.theme import page_header
from services.claim_service import ClaimService


def show_claim_form():

    page_header(
        "📝 New Insurance Claim",
        "Enter customer, vehicle and accident information."
    )

    st.info(
        """
        Complete the customer, vehicle and accident information.

        Fields marked with * are mandatory.
        """
    )

    with st.form("claim_form", clear_on_submit=False):

        # ==========================================================
        # CUSTOMER INFORMATION
        # ==========================================================

        st.markdown(
            """
            <div class="card">
            <h3>👤 Customer Information</h3>
            """,
            unsafe_allow_html=True,
        )

        col1, col2 = st.columns(2)

        with col1:
            first_name = st.text_input(
                "First Name *",
                placeholder="Enter first name",
            )

        with col2:
            last_name = st.text_input(
                "Last Name *",
                placeholder="Enter last name",
            )

        col1, col2 = st.columns(2)

        with col1:
            phone = st.text_input(
                "Mobile Number *",
                placeholder="9876543210",
            )

        with col2:
            email = st.text_input(
                "Email Address *",
                placeholder="abc@email.com",
            )

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("")

        # ==========================================================
        # VEHICLE INFORMATION
        # ==========================================================

        st.markdown(
            """
            <div class="card">
            <h3>🚗 Vehicle Information</h3>
            """,
            unsafe_allow_html=True,
        )

        registration_no = st.text_input(
            "Registration Number *",
            placeholder="MH12AB1234",
        )

        col1, col2 = st.columns(2)

        with col1:

            make = st.selectbox(
                "Vehicle Make",
                [
                    "Maruti",
                    "Hyundai",
                    "Honda",
                    "Tata",
                    "Mahindra",
                    "Toyota",
                    "Kia",
                    "MG",
                    "Skoda",
                    "Volkswagen",
                ],
            )

        with col2:

            model = st.text_input(
                "Vehicle Model *",
                placeholder="Creta",
            )

        col1, col2 = st.columns(2)

        with col1:

            year = st.selectbox(
                "Manufacturing Year",
                list(range(2026, 1999, -1)),
            )

        with col2:

            color = st.text_input(
                "Vehicle Color",
                placeholder="White",
            )

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("")

        # ==========================================================
        # CLAIM INFORMATION
        # ==========================================================

        st.markdown(
            """
            <div class="card">
            <h3>📄 Claim Information</h3>
            """,
            unsafe_allow_html=True,
        )

        accident_date = st.date_input("Accident Date")

        location = st.text_input(
            "Accident Location *",
            placeholder="City / Area",
        )

        description = st.text_area(
            "Damage Description *",
            placeholder="Describe the damage...",
            height=140,
        )

        police_case = st.checkbox("Police FIR Registered")

        towing_required = st.checkbox("Vehicle Towing Required")

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("")

        # ==========================================================
        # BUTTONS
        # ==========================================================

        col1, col2, _ = st.columns([1, 1, 4])

        with col1:
            submitted = st.form_submit_button(
                "💾 Save Claim",
                use_container_width=True,
            )

        with col2:
            clear = st.form_submit_button(
                "🗑 Clear",
                use_container_width=True,
            )

    # ==========================================================
    # CLEAR
    # ==========================================================

    if clear:
        st.rerun()

    # ==========================================================
    # SAVE CLAIM
    # ==========================================================

    if submitted:

        errors = []

        if not first_name.strip():
            errors.append("First Name is required.")

        if not last_name.strip():
            errors.append("Last Name is required.")

        if not phone.strip():
            errors.append("Mobile Number is required.")
        elif len(phone) != 10 or not phone.isdigit():
            errors.append("Enter a valid 10-digit mobile number.")

        if not email.strip():
            errors.append("Email Address is required.")
        elif "@" not in email:
            errors.append("Enter a valid email address.")

        if not registration_no.strip():
            errors.append("Registration Number is required.")

        if not model.strip():
            errors.append("Vehicle Model is required.")

        if not location.strip():
            errors.append("Accident Location is required.")

        if not description.strip():
            errors.append("Damage Description is required.")

        if errors:

            st.error("Please correct the following errors:")

            for error in errors:
                st.write(f"• {error}")

            return

        try:

            service = ClaimService()

            customer_name = f"{first_name.strip()} {last_name.strip()}"

            claim = service.create_claim(
                customer_name=customer_name,
                email=email.strip(),
                phone=phone.strip(),
                vehicle_number=registration_no.strip(),
                vehicle_brand=make,
                vehicle_model=model.strip(),
                vehicle_year=year,
                policy_number="POL-001",
                accident_date=accident_date,
                accident_location=location.strip(),
                description=description.strip(),
            )

            st.session_state["claim_id"] = claim.ClaimId
            st.session_state["page"] = "image_upload"

          

            st.rerun()

        except Exception as ex:

            st.exception(ex)