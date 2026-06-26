from datetime import datetime

from services.claim_service import ClaimService

service = ClaimService()

claim = service.create_claim(
    customer_name="Jyotsna Gupta",
    email="jyotsna@test.com",
    phone="9999999999",

    vehicle_number="KA01AB1234",
    vehicle_brand="Hyundai",
    vehicle_model="i20",
    vehicle_year=2023,
    policy_number="POL123456",

    accident_date=datetime.now(),
    accident_location="Bangalore",

    description="Front bumper damaged"
)

print(claim.ClaimId)