import os
import cv2

# Define the directory path where the images are stored
directory_path = 'testing\sharp_images'

# Define the kernel size for mean blur
kernel_size = (15, 15)

# Loop through each file in the directory
for filename in os.listdir(directory_path):
    
    # Check if the file is an image file
    if filename.endswith('.jpg') or filename.endswith('.png'):
        
        # Read the image using OpenCV
        image = cv2.imread(os.path.join(directory_path, filename))
        
        # Apply mean blur to the image
        blurred_image = cv2.blur(image, kernel_size)
        
        # Save the blurred image with a new filename
        new_filename = filename
        cv2.imwrite(os.path.join("testing\mean", new_filename), blurred_image)
