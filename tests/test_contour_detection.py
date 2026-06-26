from pathlib import Path

from ai.image_processor import ImageProcessor
from ai.damage_detector import DamageDetector


processor = ImageProcessor()
detector = DamageDetector()

image_path = Path("sample_data") / "car1.webp"

processed = processor.preprocess(image_path)

edges = detector.detect_edges(
    processed["blurred"]
)

contours = detector.find_contours(edges)

print("Contours Found:", len(contours))

output = detector.draw_contours(
    processed["original"],
    contours,
)

processor.save_image(
    output,
    "sample_data/contours_car1.jpg",
)

print("Contour image saved successfully.")