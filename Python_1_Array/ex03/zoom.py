from PIL import Image
import numpy as np

def display_image_info(path: str):
    try:
        img = Image.open(path)

        # Convert image to RGB
        img_rgb = img.convert('RGB')

        # Convert the RGB image to numpy array
        pixel_data = np.array(img_rgb)

        # Print shape of the image
        print(f"The shape of image is: {pixel_data.shape}")
        # Print pixel content of the image
        print(pixel_data)

        # Zoom into the image by taking a slice of it
        zoomed = pixel_data[0:400, 0:400, :]  # This slices the first 400 pixels on x and y axis

        # Print new shape after slicing (zooming)
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)

        # Convert back to an image and display
        zoomed_img = Image.fromarray(zoomed)
        zoomed_img.show()

    except Exception as e:
        print(f"Error processing the image: {str(e)}")


if __name__ == "__main__":
    display_image_info("animal.jpeg")
