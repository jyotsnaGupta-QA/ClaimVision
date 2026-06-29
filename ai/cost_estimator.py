class CostEstimator:
    """
    Estimates vehicle repair cost and repair time
    based on detected damage severity.
    """

    COST_MAPPING = {
        "Low": 2500,
        "Medium": 8000,
        "High": 18000,
    }

    REPAIR_TIME_MAPPING = {
        "Low": "1 Day",
        "Medium": "2 Days",
        "High": "5 Days",
    }

    def estimate(self, damages):
        """
        Estimate repair cost and repair time for each damage.
        """

        estimates = []

        for damage in damages:

            severity = damage["severity"]

            estimate = {
                "damage_id": damage["damage_id"],
                "severity": severity,
                "estimated_cost": self.COST_MAPPING.get(
                    severity,
                    0
                ),
                "repair_time": self.REPAIR_TIME_MAPPING.get(
                    severity,
                    "Unknown"
                )
            }

            estimates.append(estimate)

        return estimates

    def calculate_total_cost(self, estimates):
        """
        Calculate total repair cost.
        """

        return sum(
            estimate["estimated_cost"]
            for estimate in estimates
        )