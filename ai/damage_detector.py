import cv2


class DamageDetector:
    """
    Performs basic damage detection using OpenCV.
    """

    def detect_edges(
        self,
        image,
        low_threshold=100,
        high_threshold=200,
    ):
        """
        Detect edges using the Canny algorithm.
        """

        edges = cv2.Canny(
            image,
            low_threshold,
            high_threshold,
        )

        return edges

    def find_contours(self, edge_image):
        """
        Find contours from an edge image.
        """

        contours, hierarchy = cv2.findContours(
            edge_image,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        return contours

    def draw_contours(
        self,
        original_image,
        contours,
        color=(0, 255, 0),
        thickness=2,
    ):
        """
        Draw contours on the original image.
        """

        output = original_image.copy()

        cv2.drawContours(
            output,
            contours,
            -1,
            color,
            thickness,
        )

        return output