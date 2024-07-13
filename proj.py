import cv2

def count_vehicles(image):

  # Convert the image to grayscale.
  grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Apply Gaussian blurring to reduce noise.
  blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)

  # Apply Canny edge detection to find edges in the image.
  edges = cv2.Canny(blurred_image, 50, 150)

  # Find contours in the edges image.
  contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Get the external contours.
  external_contours = contours[0] if len(contours) == 2 else hierarchy[2]

  # Filter out small contours.
  vehicle_contours = []
  for contour in external_contours:
    area = cv2.contourArea(contour)
    if area > 100:
      vehicle_contours.append(contour)

  # Count the number of vehicle contours.
  vehicle_count = len(vehicle_contours)

  return vehicle_count

# Load the image.
image = cv2.imread('C:\Users\01\Downloads\images.jpg')

# Count the number of vehicles in the image.
vehicle_count = count_vehicles(image)

# Print the number of vehicles detected.
print("Number of vehicles detected:", vehicle_count)