import cv2


class DamageDetector:
    """
    Performs vehicle damage detection and analysis using OpenCV.
    """

    def detect_edges(
        self,
        image,
        low_threshold=50,
        high_threshold=150,
    ):
        """
        Detect edges using the Canny algorithm.
        """

        return cv2.Canny(
            image,
            low_threshold,
            high_threshold,
        )

    def find_contours(self, edge_image):
        """
        Find contours from an edge image.
        """

        contours, _ = cv2.findContours(
            edge_image,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        return contours

    def analyze_damage(
        self,
        image,
        min_area=500,
    ):
        """
        Analyze detected contours and classify
        possible damage regions.
        """

        output = image.copy()

        gray = cv2.cvtColor(
            output,
            cv2.COLOR_BGR2GRAY,
        )

        blurred = cv2.GaussianBlur(
            gray,
            (5, 5),
            0,
        )

        edges = self.detect_edges(blurred)

        contours = self.find_contours(edges)

        damages = []

        damage_id = 1

        for contour in contours:

            area = cv2.contourArea(contour)

            if area < min_area:
                continue

            x, y, w, h = cv2.boundingRect(contour)

            severity = self.calculate_severity(area)

            damages.append(
                {
                    "damage_id": damage_id,
                    "x": x,
                    "y": y,
                    "width": w,
                    "height": h,
                    "area": area,
                    "severity": severity,
                }
            )

            cv2.rectangle(
                output,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2,
            )

            damage_id += 1

        return {
            "processed_image": output,
            "damages": damages,
        }

    def calculate_severity(
        self,
        area,
    ):
        """
        Classify damage severity based on contour area.
        """

        if area < 2000:
            return "Low"

        if area < 6000:
            return "Medium"

        return "High"

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