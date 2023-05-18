import cv2
import os

# Set the path to the directory containing the images
input_dir = "testing\sharp_images"

# Set the path to the directory where the blurred images will be saved
output_dir = "testing\guassian"

# Set the kernel size for the Gaussian blur
kernel_size = (15,15)

# Loop through each file in the input directory
for filename in os.listdir(input_dir):
    # Read the image
    image = cv2.imread(os.path.join(input_dir, filename))
    
    # Apply the Gaussian blur
    blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
    
    # Write the blurred image to the output directory
    output_path = os.path.join(output_dir, filename)
    cv2.imwrite(output_path, blurred_image)
