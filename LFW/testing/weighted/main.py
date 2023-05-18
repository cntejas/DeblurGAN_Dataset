import cv2
import os

# Define the directory path containing the input images
input_dir = 'testing\sharp_images'

# Define the directory path to save the output images
output_dir = 'testing\weighted'

# Define the kernel size and weight distribution
kernel_size = (15, 15)
weight_distribution = cv2.getGaussianKernel(kernel_size[0], -1) * cv2.getGaussianKernel(kernel_size[1], -1).T

# Iterate over all files in the input directory
for filename in os.listdir(input_dir):
    # Load the input image
    input_path = os.path.join(input_dir, filename)
    img = cv2.imread(input_path)
    
    # Apply weighted blur
    blurred = cv2.filter2D(img, -1, weight_distribution, anchor=(kernel_size[0]//2,kernel_size[1]//2))
    
    # Save the output image
    output_path = os.path.join(output_dir,filename)
    cv2.imwrite(output_path, blurred)
