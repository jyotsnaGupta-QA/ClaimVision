from ai.fraud_detector import FraudDetector


def test_fraud_detector():

    detector = FraudDetector()

    damages = [
        {
            "damage_id": 1,
            "severity": "High"
        },
        {
            "damage_id": 2,
            "severity": "Medium"
        },
        {
            "damage_id": 3,
            "severity": "High"
        }
    ]

    estimates = [
        {
            "damage_id": 1,
            "estimated_cost": 18000
        },
        {
            "damage_id": 2,
            "estimated_cost": 8000
        },
        {
            "damage_id": 3,
            "estimated_cost": 18000
        }
    ]

    result = detector.assess(
        damages,
        estimates
    )

    assert result["fraud_score"] > 0
    assert result["risk_level"] == "Medium"

    print("\n===== Fraud Detection =====")
    print(f"Fraud Score : {result['fraud_score']}")
    print(f"Risk Level  : {result['risk_level']}")

    print("\nReasons:")

    for reason in result["reasons"]:
        print(f"- {reason}")

    print("\n✅ Fraud Detector Test Passed!")