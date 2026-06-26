from pathlib import Path
import cv2


class ImageProcessor:
    """
    Handles all image preprocessing operations for ClaimVision.
    """

    DEFAULT_WIDTH = 800
    DEFAULT_KERNEL = (5, 5)

    def load_image(self, image_path: str):
        """
        Load image from disk.
        """

        image_path = Path(image_path)

        if not image_path.exists():
            raise FileNotFoundError(
                f"Image not found: {image_path}"
            )

        image = cv2.imread(str(image_path))

        if image is None:
            raise ValueError(
                f"Unable to load image: {image_path}"
            )

        return image

    def resize_image(
        self,
        image,
        width: int = DEFAULT_WIDTH
    ):
        """
        Resize image while maintaining aspect ratio.
        """

        original_height = image.shape[0]
        original_width = image.shape[1]

        aspect_ratio = original_height / original_width

        height = int(width * aspect_ratio)

        resized = cv2.resize(
            image,
            (width, height)
        )

        return resized

    def convert_to_rgb(self, image):
        """
        Convert BGR image to RGB.
        """

        return cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB
        )

    def convert_to_gray(self, image):
        """
        Convert image to grayscale.
        """

        return cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

    def remove_noise(
        self,
        image,
        kernel_size=DEFAULT_KERNEL
    ):
        """
        Apply Gaussian Blur.
        """

        return cv2.GaussianBlur(
            image,
            kernel_size,
            0
        )

    def detect_edges(
        self,
        image,
        threshold1=50,
        threshold2=150
    ):
        """
        Detect edges using Canny Edge Detection.
        """

        return cv2.Canny(
            image,
            threshold1,
            threshold2
        )

    def detect_contours(
        self,
        edge_image
    ):
        """
        Detect contours from edge image.
        """

        contours, _ = cv2.findContours(
            edge_image,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        return contours

    def detect_damage_regions(
        self,
        image,
        min_area=500
    ):
        """
        Detect possible damage regions by filtering contours
        and drawing bounding boxes.
        """

        output = image.copy()

        gray = self.convert_to_gray(output)

        blurred = self.remove_noise(gray)

        edges = self.detect_edges(blurred)

        contours = self.detect_contours(edges)

        for contour in contours:

            area = cv2.contourArea(contour)

            if area >= min_area:

                x, y, w, h = cv2.boundingRect(contour)

                cv2.rectangle(
                    output,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

        return output

    def save_image(
        self,
        image,
        output_path: str
    ):
        """
        Save image to disk.
        """

        cv2.imwrite(
            output_path,
            image
        )

    def preprocess(
        self,
        image_path: str
    ):
        """
        Complete preprocessing pipeline.
        """

        image = self.load_image(image_path)

        image = self.resize_image(image)

        rgb_image = self.convert_to_rgb(image)

        gray_image = self.convert_to_gray(image)

        blurred_image = self.remove_noise(gray_image)

        edges = self.detect_edges(blurred_image)

        contours = self.detect_contours(edges)

        damage_regions = self.detect_damage_regions(image)

        return {
            "original": image,
            "rgb": rgb_image,
            "gray": gray_image,
            "blurred": blurred_image,
            "edges": edges,
            "contours": contours,
            "damage_regions": damage_regions
        }