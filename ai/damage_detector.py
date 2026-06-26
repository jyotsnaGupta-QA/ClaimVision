import cv2


class DamageDetector:
    """
    Performs basic damage detection using OpenCV.
    """

    def detect_edges(
        self,
        image,
        low_threshold=100,
        high_threshold=200
    ):
        """
        Detect edges using the Canny algorithm.
        """

        edges = cv2.Canny(
            image,
            low_threshold,
            high_threshold
        )

        return edges