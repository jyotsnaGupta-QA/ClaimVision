from pathlib import Path

from ai.image_processor import ImageProcessor


def test_image_processor():

    processor = ImageProcessor()

    image_path = Path("sample_data") / "car1.webp"

    result = processor.preprocess(image_path)

    assert result["original"] is not None
    assert result["rgb"] is not None
    assert result["gray"] is not None
    assert result["blurred"] is not None

    print("\n✅ Image Processor Working Successfully!")