class FraudDetector:
    """
    Calculates a fraud risk score based on
    detected damages and repair estimates.
    """

    def assess(self, damages, estimates):
        """
        Assess fraud risk.
        """

        fraud_score = 0
        reasons = []

        # Rule 1: Number of damage regions
        if len(damages) > 3:
            fraud_score += 10
            reasons.append("Multiple damage regions detected.")

        # Rule 2: Total repair cost
        total_cost = sum(
            estimate["estimated_cost"]
            for estimate in estimates
        )

        if total_cost > 20000:
            fraud_score += 20
            reasons.append("High repair cost.")

        # Rule 3: High severity damages
        high_damage_count = sum(
            1
            for damage in damages
            if damage["severity"] == "High"
        )

        fraud_score += high_damage_count * 20

        if high_damage_count:
            reasons.append(
                f"{high_damage_count} high severity damage(s)."
            )

        # Cap fraud score at 100
        fraud_score = min(fraud_score, 100)

        # Determine risk level
        if fraud_score <= 30:
            risk_level = "Low"
        elif fraud_score <= 60:
            risk_level = "Medium"
        else:
            risk_level = "High"

        return {
            "fraud_score": fraud_score,
            "risk_level": risk_level,
            "reasons": reasons,
        }