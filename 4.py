import cv2
import numpy as np

# Define the dimensions of the canvas
canvas_width = 500
canvas_height = 500

# Create a blank canvas
canvas = np.ones((canvas_height, canvas_width, 3), dtype=np.uint8) * 255

# Define the initial object (a square)
obj_points = np.array([[100, 100], [200, 100], [200, 200], [100, 200]], dtype=np.int32)

# Define the transformation matrices
translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])
rotation_matrix = cv2.getRotationMatrix2D((150, 150), 45, 1)
scaling_matrix = np.float32([[1.5, 0, 0], [0, 1.5, 0]])

# Apply transformations
translated_obj = np.array([np.dot(translation_matrix, [x, y, 1])[:2] for x, y in obj_points], dtype=np.int32)
rotated_obj = np.array([np.dot(rotation_matrix, [x, y, 1])[:2] for x, y in translated_obj], dtype=np.int32)
scaled_obj = np.array([np.dot(scaling_matrix, [x, y, 1])[:2] for x, y in rotated_obj], dtype=np.int32)

# Draw the objects on the canvas
cv2.polylines(canvas, [obj_points], True, (0, 0, 0), 2)
cv2.polylines(canvas, [translated_obj], True, (0, 255, 0), 2)
cv2.polylines(canvas, [rotated_obj], True, (255, 0, 0), 2)
cv2.polylines(canvas, [scaled_obj], True, (0, 0, 255), 2)

# Display the canvas
cv2.imshow("2D Transformations", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
