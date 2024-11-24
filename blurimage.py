import cv2
import numpy as np

# Load an image from file
image_path = 'num_plate_cropped.jpg'
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is not None:
    # Apply Gaussian blur to the image
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    
    # Calculate the unsharp mask
    unsharp_mask = cv2.subtract(image, blurred_image)
    
    # Add the unsharp mask back to the original image
    sharpened_image = cv2.addWeighted(blurred_image, 1.5, unsharp_mask, -0.5, 0)
    
    # Convert the sharpened image to grayscale
    gray_sharpened_image = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2GRAY)
    
    # Apply binary threshold to make it black and white
    _, binary_image = cv2.threshold(gray_sharpened_image, 128, 255, cv2.THRESH_BINARY)
    
    
    cv2.imwrite('binary_image.jpg', binary_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed to load the image.")
