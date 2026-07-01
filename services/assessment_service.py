from ai.image_processor import ImageProcessor
from ai.damage_detector import DamageDetector
from ai.cost_estimator import CostEstimator
from ai.fraud_detector import FraudDetector
from models.assessment_result import AssessmentResult
from database.models import DamageAssessment
from database.repository import ClaimRepository


class AssessmentService:
    """
    Coordinates the complete AI assessment workflow.
    """

    def __init__(self):

        self.processor = ImageProcessor()
        self.detector = DamageDetector()
        self.estimator = CostEstimator()
        self.fraud_detector = FraudDetector()

    def assess(
        self,
        image_path,
    ):
        """
        Perform complete vehicle damage assessment.
        """

        # Image preprocessing
        processed = self.processor.preprocess(image_path)

        # Damage analysis
        damage_result = self.detector.analyze_damage(
            processed["original"]
        )

        damages = damage_result["damages"]

        # Cost estimation
        estimates = self.estimator.estimate(damages)

        total_cost = self.estimator.calculate_total_cost(
            estimates
        )

        # Fraud assessment
        fraud = self.fraud_detector.assess(
            damages,
            estimates,
        )

        return AssessmentResult(
            processed_image=damage_result["processed_image"],
            damages=damages,
            estimates=estimates,
            total_cost=total_cost,
            fraud=fraud,
        )
    

    def save_assessment(
        self,
        claim_id,
        result,
        processed_image_path=None,
    ):

        repo = ClaimRepository()

        try:

            fraud_score = result.fraud["fraud_score"]

            if fraud_score < 30:
                recommendation = "Approve Claim"
            elif fraud_score < 70:
                recommendation = "Manual Review"
            else:
                recommendation = "High Fraud Risk"

            assessment = DamageAssessment(
                ClaimId=claim_id,
                DamageType="Vehicle Damage",
                Severity=(
                    result.damages[0]["severity"]
                    if result.damages
                    else "None"
                ),
                EstimatedCost=result.total_cost,
                FraudScore=fraud_score,
                Recommendation=recommendation,
                Confidence=0.95,
                ProcessedImagePath=processed_image_path,
            )

            repo.create_damage_assessment(
                assessment
            )

        finally:

            repo.close()