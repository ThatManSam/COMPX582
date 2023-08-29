import os
import sys

from PIL import Image

def upscale_image(input_path, output_path, target_size):
    try:
        # Open the input image
        input_image = Image.open(input_path)

        # Get the original image dimensions
        original_width, original_height = input_image.size

        # Upscale the image using nearest-neighbor interpolation (pixel replication)
        upscaled_image = input_image.resize((target_size, target_size), Image.NEAREST)

        # Save the upscaled image to the output path
        upscaled_image.save(output_path)
        print("Image successfully upscaled and saved to:", output_path)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    output_image_dir = "./images/upscaled/"
    if not os.path.exists(output_image_dir):
        os.makedirs(output_image_dir)
    target_size = 1000
    
    for i in range(10):
        input_image_path = f"../apriltag-imgs/tagStandard52h13/tag52_13_0000{i}.png"
        output_image_path = f"{output_image_dir}tag52_13_0000{i}_upscaled.png"
        upscale_image(input_image_path, output_image_path, target_size)
