import numpy as np

def ft_invert(array: np.array) -> np.array:
    # Inverting each color channel
    inverted = 255 - array
    return inverted

def ft_red(array: np.array) -> np.array:
    # Keeping only the red channel
    red = array * [1, 0, 0]
    return red

def ft_green(array: np.array) -> np.array:
    # Keeping only the green channel
    green = array.copy()
    green[:, :, 0] = 0    # Red
    green[:, :, 2] = 0    # Blue
    return green

def ft_blue(array: np.array) -> np.array:
    # Keeping only the blue channel
    blue = array * [0, 0, 1]
    return blue

def ft_grey(array: np.array) -> np.array:
    # Averaging the RGB channels
    grey_value = np.mean(array, axis=-1, keepdims=True)
    grey = np.repeat(grey_value, 3, axis=-1)
    return grey
