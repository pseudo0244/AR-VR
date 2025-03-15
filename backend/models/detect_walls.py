import cv2
import numpy as np
import json

def detect(binary_img, min_wall_area=500):
    """
    Detects walls in a binary floor plan image.

    Parameters:
        binary_img (numpy array): Black & white processed image.
        min_wall_area (int): Minimum area threshold to filter small noise.

    Returns:
        list: List of wall bounding boxes [(x, y, w, h), ...]
    """

    # Find contours (walls)
    contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    walls = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)  # Get bounding box
        
        # Filter out small noise
        if w * h > min_wall_area:
            walls.append((x, y, w, h))

    return walls

if __name__ == "__main__":
    # Load and process test image
    img_path = "floorplan.png"  # Replace with your image
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Convert to binary (if not already processed)
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

    # Detect walls
    detected_walls = detect(binary)

    # Save wall data as JSON
    with open("walls.json", "w") as f:
        json.dump(detected_walls, f)

    print("Walls saved to walls.json!")

    # Draw walls for visualization
    output_img = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
    for (x, y, w, h) in detected_walls:
        cv2.rectangle(output_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the result
    cv2.imshow("Detected Walls", output_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
