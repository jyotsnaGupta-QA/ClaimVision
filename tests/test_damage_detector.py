from pathlib import Path

import cv2

from ai.damage_detector import DamageDetector
from ai.image_processor import ImageProcessor


def test_damage_detector():

    processor = ImageProcessor()
    detector = DamageDetector()

    image_path = Path("sample_data") / "car1.webp"

    # Load and preprocess image
    result = processor.preprocess(image_path)

    # Analyze damage
    analysis = detector.analyze_damage(
        result["original"]
    )

    # Verify results
    assert analysis is not None
    assert "processed_image" in analysis
    assert "damages" in analysis

    processed_image = analysis["processed_image"]
    damages = analysis["damages"]

    assert processed_image is not None
    assert isinstance(damages, list)

    # Save output image
    output_path = Path("sample_data") / "damage_analysis_car1.jpg"

    processor.save_image(
        processed_image,
        str(output_path)
    )

    assert output_path.exists()

    print("\n===== Damage Detection Result =====")

    if damages:

        for damage in damages:

            print(
                f"Damage #{damage['damage_id']}"
            )

            print(
                f"Area      : {damage['area']:.2f}"
            )

            print(
                f"Location  : ({damage['x']}, {damage['y']})"
            )

            print(
                f"Size      : {damage['width']} x {damage['height']}"
            )

            print(
                f"Severity  : {damage['severity']}"
            )

            print("------------------------------")

    else:

        print("No significant damage regions detected.")

    print("\n✅ Damage Detector Test Passed!")