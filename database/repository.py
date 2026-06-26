from database.db import SessionLocal
from database.models import (
    Customer,
    Vehicle,
    Claim,
    UploadedImage
)


class ClaimRepository:

    def __init__(self):
        self.db = SessionLocal()

    def create_customer(self, customer: Customer):

        self.db.add(customer)
        self.db.commit()
        self.db.refresh(customer)

        return customer

    def create_vehicle(self, vehicle: Vehicle):

        self.db.add(vehicle)
        self.db.commit()
        self.db.refresh(vehicle)

        return vehicle

    def create_claim(self, claim: Claim):

        self.db.add(claim)
        self.db.commit()
        self.db.refresh(claim)

        return claim
    
    def create_uploaded_image(self, claim_id, image_path):
        image = UploadedImage(
            ClaimId=claim_id,
            ImagePath=image_path
        )

        self.db.add(image)
        self.db.commit()
        self.db.refresh(image)

        return image

    def close(self):
        self.db.close()