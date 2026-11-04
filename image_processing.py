
import cv2
from pathlib import Path

# Load the input image
image_path = "input.jpg"
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(
        "Please add an image named input.jpg"
    )

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges
edges = cv2.Canny(blurred, 50, 150)

# Save the results
Path("results").mkdir(exist_ok=True)

cv2.imwrite("results/grayscale.jpg", gray)
cv2.imwrite("results/blurred.jpg", blurred)
cv2.imwrite("results/edges.jpg", edges)

print("Image processing completed!")
