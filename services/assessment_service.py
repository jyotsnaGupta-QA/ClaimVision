from ai.image_processor import ImageProcessor
from ai.damage_detector import DamageDetector
from ai.cost_estimator import CostEstimator
from ai.fraud_detector import FraudDetector
from models.assessment_result import AssessmentResult


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