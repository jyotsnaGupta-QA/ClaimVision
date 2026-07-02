import os
import uuid

from datetime import datetime

from database.models import Customer, Vehicle, Claim
from database.repository import ClaimRepository


class ClaimService:

    def __init__(self):
        self.repo = ClaimRepository()

    def save_uploaded_image(self, claim_id, image_path):
        return self.repo.create_uploaded_image(
            claim_id,
            image_path
        )

    def upload_image(self, claim_id, uploaded_file):
        """
        Save uploaded image to disk and store its path in the database.
        """

        # Create uploads folder if it doesn't exist
        upload_folder = "uploads"
        os.makedirs(upload_folder, exist_ok=True)

        # Get file extension
        extension = uploaded_file.name.split(".")[-1].lower()

        # Generate unique filename
        unique_filename = f"{uuid.uuid4()}.{extension}"

        # Full image path
        image_path = os.path.join(upload_folder, unique_filename)

        # Save image to disk
        with open(image_path, "wb") as file:
            file.write(uploaded_file.getbuffer())

        # Save image path in database
        self.repo.create_uploaded_image(
            claim_id=claim_id,
            image_path=image_path
        )

        return image_path

    def create_claim(
        self,
        customer_name,
        email,
        phone,
        vehicle_number,
        vehicle_brand,
        vehicle_model,
        vehicle_year,
        policy_number,
        accident_date,
        accident_location,
        description
    ):

        try:

            if not isinstance(accident_date, datetime):
                accident_date = datetime.combine(
                    accident_date,
                    datetime.min.time()
                )

            customer = Customer(
                FullName=customer_name,
                Email=email,
                PhoneNumber=phone
            )

            customer = self.repo.create_customer(customer)

            vehicle = Vehicle(
                CustomerId=customer.CustomerId,
                VehicleNumber=vehicle_number,
                VehicleBrand=vehicle_brand,
                VehicleModel=vehicle_model,
                VehicleYear=vehicle_year,
                InsurancePolicyNumber=policy_number
            )

            vehicle = self.repo.create_vehicle(vehicle)

            claim = Claim(
                CustomerId=customer.CustomerId,
                VehicleId=vehicle.VehicleId,
                AccidentDate=accident_date,
                AccidentLocation=accident_location,
                Description=description,
                Status="Submitted"
            )

            claim = self.repo.create_claim(claim)

            return claim

        finally:
            self.repo.close()