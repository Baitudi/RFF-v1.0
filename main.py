# main.py
import cv2
from utils.graph_parser import load_image, extract_playing_area, extract_inner_wall, extract_outer_wall, extract_expiration_line, extract_player
from utils.flywheel_logic import find_player_center, dummy_route
from utils.visualizer import visualize

image_path = 'data/your_screenshot.png'  # Put screenshot here
img = load_image(image_path)

# Extract components
playing_area = extract_playing_area(img)
inner_wall = extract_inner_wall(img)
outer_wall = extract_outer_wall(img)
expiration_lines = extract_expiration_line(img)
player_mask = extract_player(img)

# Get player center
player_center = find_player_center(player_mask)
if player_center == (0, 0):
    print("⚠️  Warning: Player not detected properly, using fallback position.")
    player_center = (100, 100)

# Define dummy destination manually for now
destination = (player_center[0] + 100, player_center[1] + 100)

# Compute Route
route = dummy_route(player_center, destination)

# Visualize
output = visualize(img, playing_area, inner_wall, outer_wall, expiration_lines, player_mask, route)

cv2.imshow("RFF - Phase1 Cleaned", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
