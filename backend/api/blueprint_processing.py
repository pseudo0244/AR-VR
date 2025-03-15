import cv2
from backend.models import detect_walls  # Correct package import

def process_blueprint(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Convert to binary
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

    # Detect walls
    walls = detect_walls.detect(binary)

    return walls

if __name__ == "__main__":
    image_path = "backend/models/floorplan.png"  # Update with your image path
    detected_walls = process_blueprint(image_path)
    print(detected_walls)  # Print wall coordinates
