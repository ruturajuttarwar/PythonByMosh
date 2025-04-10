import cv2
import numpy as np

# Step 1: Read the image
image_path = '/Users/ruturajuttarwar/Desktop/First_Robotics_2025.jpeg'  # Replace with your image file path
image = cv2.imread(image_path)

# Step 2: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # Step 3: Apply GaussianBlur to reduce noise and improve edge detection
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# # Step 4: Apply Canny edge detection
edges = cv2.Canny(blurred_image, 100, 200)  # You can adjust the thresholds (100, 200)

# Step 5: Show the original and edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
