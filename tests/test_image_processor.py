from pathlib import Path

from ai.image_processor import ImageProcessor


def test_image_processor():

    processor = ImageProcessor()

    image_path = Path("sample_data") / "car1.webp"

    result = processor.preprocess(image_path)

    # Verify preprocessing results
    assert result["original"] is not None
    assert result["rgb"] is not None
    assert result["gray"] is not None
    assert result["blurred"] is not None
    assert result["edges"] is not None
    assert result["damage_regions"] is not None

    # Save processed output for visual verification
    output_path = Path("sample_data") / "damage_regions_car1.jpg"

    processor.save_image(
        result["damage_regions"],
        str(output_path)
    )

    # Verify output image was created
    assert output_path.exists()

    print("\n✅ Image Processor Working Successfully!")
    print(f"✅ Damage region image saved to: {output_path}")