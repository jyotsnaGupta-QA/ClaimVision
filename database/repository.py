from database.db import SessionLocal

from database.models import (
    Customer,
    Vehicle,
    Claim,
    UploadedImage,
    DamageAssessment,
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
    
    def get_uploaded_images(self, claim_id):

        return (
            self.db.query(UploadedImage)
            .filter(UploadedImage.ClaimId == claim_id)
            .order_by(UploadedImage.UploadedDate.desc())
            .all()
        )
    
    def create_uploaded_image(self, claim_id, image_path):
        image = UploadedImage(
            ClaimId=claim_id,
            ImagePath=image_path
        )

        self.db.add(image)
        self.db.commit()
        self.db.refresh(image)

        return image
    
    def create_damage_assessment(self, assessment):

        self.db.add(assessment)
        self.db.commit()
        self.db.refresh(assessment)

        return assessment
    
   
    def get_damage_assessments(self, claim_id):

        return (
            self.db.query(DamageAssessment)
            .filter(DamageAssessment.ClaimId == claim_id)
            .order_by(DamageAssessment.CreatedDate.desc())
            .all()
        )
    
    def get_all_damage_assessments(self):

        return (
            self.db.query(DamageAssessment)
            .order_by(
                DamageAssessment.CreatedDate.desc()
            )
            .all()
        )
    
    def get_total_claims(self):

        return self.db.query(Claim).count()


    def get_total_assessments(self):

        return self.db.query(DamageAssessment).count()


    def get_total_estimated_cost(self):

        assessments = self.db.query(DamageAssessment).all()

        return sum(
            float(a.EstimatedCost or 0)
            for a in assessments
        )


    def get_average_fraud_score(self):

        assessments = self.db.query(DamageAssessment).all()

        if not assessments:
            return 0

        total = sum(
            float(a.FraudScore or 0)
            for a in assessments
        )

        return round(
            total / len(assessments),
            2,
        )
    def get_recent_claims(self):

        claims = (
            self.db.query(Claim, Customer, Vehicle)
            .join(Customer, Claim.CustomerId == Customer.CustomerId)
            .join(Vehicle, Claim.VehicleId == Vehicle.VehicleId)
            .order_by(Claim.CreatedDate.desc())
            .limit(5)
            .all()
        )

        rows = []

        for claim, customer, vehicle in claims:

            rows.append(
                {
                    "Claim ID": claim.ClaimId,
                    "Customer": customer.FullName,
                    "Vehicle": f"{vehicle.VehicleBrand} {vehicle.VehicleModel}",
                    "Status": claim.Status,
                }
            )

        return rows
    
    def get_ai_summary(self):

        assessments = self.db.query(DamageAssessment).all()

        high = 0
        medium = 0
        low = 0
        fraud = []

        for a in assessments:

            severity = (a.Severity or "").lower()

            if severity == "high":
                high += 1

            elif severity == "medium":
                medium += 1

            else:
                low += 1

            fraud.append(float(a.FraudScore or 0))

        avg_fraud = round(sum(fraud) / len(fraud), 2) if fraud else 0

        return {
            "high": high,
            "medium": medium,
            "low": low,
            "fraud": avg_fraud,
        }
    
    def get_claim_status_summary(self):

        total = self.db.query(Claim).count()

        if total == 0:

            return {
                "completed": 0,
            }

        completed = (
            self.db.query(Claim)
            .filter(Claim.Status == "Completed")
            .count()
        )

        return {
            "completed": round(completed * 100 / total),
        }

    def close(self):
        self.db.close()