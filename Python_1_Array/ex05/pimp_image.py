import numpy as np
from load_image import ft_load
from PIL import Image

def ft_invert(array: np.array) -> np.array:
    inverted = 255 - array
    return inverted

def ft_red(array: np.array) -> np.array:
    red = array * [1, 0, 0]
    return red

def ft_green(array: np.array) -> np.array:
    green = array.copy()
    green[:, :, 0] = 0    # Red
    green[:, :, 2] = 0    # Blue
    return green

def ft_blue(array: np.array) -> np.array:
    blue = array * [0, 0, 1]
    return blue

def ft_grey(array: np.array) -> np.array:
    grey_value = np.mean(array, axis=-1, keepdims=True)
    grey = np.repeat(grey_value, 3, axis=-1)
    return grey


if __name__ == "__main__":
    array_ = ft_load("landscape.jpg")
    img_ = Image.fromarray(array_.astype(np.uint8))
    img_.show()
    arr_1 = ft_invert(array_)
    img_1 = Image.fromarray(arr_1.astype(np.uint8))
    img_1.show()
    arr_2 = ft_red(array_)
    img_2 = Image.fromarray(arr_2.astype(np.uint8))
    img_2.show()
    arr_3 = ft_green(array_)
    img_3 = Image.fromarray(arr_3.astype(np.uint8))
    img_3.show()
    arr_4 = ft_blue(array_)
    img_4 = Image.fromarray(arr_4.astype(np.uint8))
    img_4.show()
    arr_5 = ft_grey(array_)
    img_5 = Image.fromarray(arr_5.astype(np.uint8))
    img_5.show()
