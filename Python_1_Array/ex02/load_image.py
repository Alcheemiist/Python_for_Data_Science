from PIL import Image
import numpy as np

def ft_load(path: str) -> np.array:
    try:
        img = Image.open(path)

        if img.format not in ["JPEG", "JPG"]:
            raise ValueError(f"Unsupported image format: {img.format}. Supported formats are JPG and JPEG.")

        print(f"Image format: {img.format}")

        img_rgb = img.convert('RGB')

        pixel_data = np.array(img_rgb)
        
        for row in pixel_data:
            for pixel in row:
                print(pixel)

        return pixel_data

    except Exception as e:
        raise RuntimeError(f"Error loading the image: {str(e)}")

# img_array = ft_load('path_to_your_image.jpg')
