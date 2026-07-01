from pathlib import Path

from services.assessment_service import AssessmentService


def test_assessment_service():

    service = AssessmentService()

    image_path = Path("sample_data") / "car1.webp"

    result = service.assess(image_path)

    assert result is not None

    assert "processed_image" in result
    assert "damages" in result
    assert "estimates" in result
    assert "total_cost" in result
    assert "fraud" in result

    print("\n===== Assessment Summary =====")

    print(f"Damage Regions : {len(result['damages'])}")
    print(f"Estimated Cost : ₹{result['total_cost']}")
    print(
        f"Fraud Score    : {result['fraud']['fraud_score']}"
    )
    print(
        f"Risk Level     : {result['fraud']['risk_level']}"
    )

    print("\n✅ Assessment Service Test Passed!")