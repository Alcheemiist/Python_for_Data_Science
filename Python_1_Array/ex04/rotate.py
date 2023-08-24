from PIL import Image
import numpy as np
from load_image import ft_load, zoom


def rotate(zoomed_image: np.array) -> None:
    # print("--------------\n")
    transpose_arr = np.zeros((zoomed_image.shape[1], zoomed_image.shape[0]))
    assert transpose_arr is not None, "Error creating empty array."
    for i in range(zoomed_image.shape[0]):
        for j in range(zoomed_image.shape[1]):
            transpose_arr[j, i] = zoomed_image[i, j]
    # print("transpose_arr : \n", transpose_arr)
    np__ = np.array(transpose_arr)
    zoomed_img = Image.fromarray(np__.astype(np.uint8))
    # zoomed_img.show()


if __name__ == "__main__":
    rotate(zoom(ft_load("animal.jpeg")))
