from ai.cost_estimator import CostEstimator


def test_cost_estimator():

    estimator = CostEstimator()

    damages = [
        {
            "damage_id": 1,
            "severity": "Low"
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

    estimates = estimator.estimate(damages)

    assert len(estimates) == 3

    assert estimates[0]["estimated_cost"] == 2500
    assert estimates[0]["repair_time"] == "1 Day"

    assert estimates[1]["estimated_cost"] == 8000
    assert estimates[1]["repair_time"] == "2 Days"

    assert estimates[2]["estimated_cost"] == 18000
    assert estimates[2]["repair_time"] == "5 Days"

    total_cost = estimator.calculate_total_cost(estimates)

    assert total_cost == 28500

    print("\n===== Cost Estimation =====")

    for estimate in estimates:

        print(
            f"Damage #{estimate['damage_id']}"
        )

        print(
            f"Severity       : {estimate['severity']}"
        )

        print(
            f"Estimated Cost : ₹{estimate['estimated_cost']}"
        )

        print(
            f"Repair Time    : {estimate['repair_time']}"
        )

        print("----------------------------")

    print(f"\nTotal Cost : ₹{total_cost}")

    print("\n✅ Cost Estimator Test Passed!")