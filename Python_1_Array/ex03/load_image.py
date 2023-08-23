from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    img = Image.open(path)
    assert img is not None, "Image not found."
    assert img.format in ["JPEG", "JPG"], \
        "Unsupported image format: ${format}.".format(format=img.format)
    img_rgb = img.convert('RGB')
    assert img_rgb is not None, "Error converting image to RGB."
    pixel_data = np.array(img_rgb)
    print("The shape of image is: ", pixel_data.shape)
    return pixel_data
