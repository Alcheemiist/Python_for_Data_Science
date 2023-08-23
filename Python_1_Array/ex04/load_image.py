from PIL import Image
import numpy as np


def ft_load(path: str) -> Image.Image:
    img = Image.open(path)
    assert img is not None, "Image not found."
    assert img.format in ["JPEG", "JPG"], \
        "Unsupported image format: ${format}.".format(format=img.format)
    img_rgb = img.convert('RGB')
    assert img_rgb is not None, "Error converting image to RGB."
    pixel_data = np.array(img_rgb)
    # print("The shape of image is: ", pixel_data.shape)
    return pixel_data

def zoom(image: np.array) -> np.array:
    zoomed = image[100:500, 410:810, 0]
    assert zoomed is not None, "Error slicing image."
    print("The shape of image is : ", zoomed.shape)
    transformed_array = zoomed.reshape(-1, 1, 1)
    print(transformed_array)
    zoomed_img = Image.fromarray(zoomed)
    zoomed_img.show()
    return transformed_array