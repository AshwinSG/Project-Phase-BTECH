import cv2
import pytesseract

# Load the image using OpenCV
image1 = cv2.imread("num_plate_original.jpg")

text = pytesseract.image_to_string(image1,config='--psm 6')

# Print the extracted text
print(text)
