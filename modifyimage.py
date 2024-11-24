import cv2
import numpy as np

image_path = 'num_plate_cropped.jpg'

# Read the image
image = cv2.imread(image_path)

if image is None:
    print("Image not found or couldn't be loaded.")
else:
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)   
    sharpening_kernel = np.array([[-2, -3, -2],
                                  [-2, 26, -2],
                                  [-2, -3, -2]])

    sharpened_image = cv2.filter2D(blurred_image, -1, sharpening_kernel)

    threshold_value = 128  # Adjust this value as needed
    _, binary_image = cv2.threshold(sharpened_image, threshold_value, 255, cv2.THRESH_BINARY)

    cv2.imshow("Original", image)
    cv2.imshow("Blurred", blurred_image)
    cv2.imshow("Sharpened", sharpened_image)
    cv2.imshow("Binary",binary_image)

    while True:
        key = cv2.waitKey(1)  
        if key == ord('q') or key == 27:  
            break

    cv2.destroyAllWindows()
