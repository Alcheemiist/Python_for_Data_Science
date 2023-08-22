from PIL import Image
import numpy as np

def process_image(path: str):
    try:
        img = Image.open(path)
        img_gray = img.convert('L')
        square_img = img_gray.crop((0, 0, 400, 400)) 
        transposed_img = square_img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90)
        transposed_data = np.array(transposed_img)

        print(f"The shape of image is: {transposed_data.shape}")

        print(transposed_data)

        transposed_img.show()

    except Exception as e:
        print(f"Error processing the image: {str(e)}")


if __name__ == "__main__":
    process_image("animal.jpeg")
