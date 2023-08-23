from PIL import Image
import numpy as np
from load_image import ft_load
from load_image import zoom

def zoom_(img: Image.Image, size=(400, 400)) -> Image.Image:
    left = 480
    right = left + size[0]
    top = 100
    bottom = top + size[1]
    image_ = img.crop((left, top, right, bottom))
    image_.show()
    return image_

def rotate(img: Image.Image):
    img_arr = np.array(img)  # Convert image to numpy array
    
    # Initialize a transposed image with zeros
    transposed = np.zeros((img_arr.shape[1], img_arr.shape[0], img_arr.shape[2]))

    # Fill in the transposed img
    for i in range(img_arr.shape[0]):
        for j in range(img_arr.shape[1]):
            for k in range(img_arr.shape[2]):
                transposed[j, i, k] = img_arr[i, j, k]

    # Squeeze out singleton dimensions
    transposed_squeezed = np.squeeze(transposed)

    # Convert numpy array back to PIL Image and show
    _img = Image.fromarray(transposed_squeezed.astype(np.uint8))
    _img.show()



if __name__ == "__main__":
    image = ft_load("animal.jpeg")
    zoomed_image = zoom(image)
    rotate(zoomed_image)