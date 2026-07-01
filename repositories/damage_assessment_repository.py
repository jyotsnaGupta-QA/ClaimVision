from database.db_connection import SessionLocal
from models.damage_assessment import DamageAssessment


class DamageAssessmentRepository:
    """
    Repository for DamageAssessment operations.
    """

    def save(self, assessment: DamageAssessment):

        session = SessionLocal()

        try:
            session.add(assessment)
            session.commit()
            session.refresh(assessment)

            return assessment

        finally:
            session.close()