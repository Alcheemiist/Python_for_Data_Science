from PIL import Image
import numpy as np
from load_image import ft_load


def zoom(image: np.array):
    zoomed = image[100:500, 410:810, 0]
    assert zoomed is not None, "Error slicing image."
    print("New shape after slicing: ", zoomed.shape)
    transformed_array = zoomed.reshape(-1, 1, 1)
    print(transformed_array)
    zoomed_img = Image.fromarray(zoomed)
    zoomed_img.show()


if __name__ == "__main__":
    image = ft_load("animal.jpeg")
    print(image)
    zoom(image)
