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
    # print("The loaded shape of image is: ", pixel_data.shape)
    # print("returning pixel data type : ", type(pixel_data))
    # print("DATA : ", pixel_data)
    image_ = Image.fromarray(pixel_data)
    # image_.show()
    return pixel_data

def zoom(image: np.array) -> np.array:
    zoomed = image[100:500, 410:810, 1]
    assert zoomed is not None, "Error slicing image."
    # print("returning zoomed data type : ", type(zoomed))
    print("The shape of image is : ", zoomed.shape)
    transformed_array = (zoomed.reshape(-1,1,1))
    print("\n", transformed_array)
    zoomed_img = Image.fromarray(zoomed)
    # zoomed_img.show()
    return zoomed
