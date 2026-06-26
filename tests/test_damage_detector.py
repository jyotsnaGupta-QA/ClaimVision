from pathlib import Path

from ai.image_processor import ImageProcessor
from ai.damage_detector import DamageDetector


processor = ImageProcessor()
detector = DamageDetector()

image_path = Path("sample_data") / "car1.webp"

processed = processor.preprocess(image_path)

# Detect edges
edges = detector.detect_edges(
    processed["blurred"]
)

print("Edge Detection Successful!")

print("Edge Image Shape:", edges.shape)

# Save edge image
processor.save_image(
    edges,
    "sample_data/edges_car1.jpg"
)

print("Edge image saved successfully.")