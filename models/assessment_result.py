from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class AssessmentResult:
    """
    DTO representing the complete AI assessment result.
    """

    processed_image: Any
    damages: List[Dict]
    estimates: List[Dict]
    total_cost: float
    fraud: Dict