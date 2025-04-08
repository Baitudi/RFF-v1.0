import cv2
import random
from visual.fork_heatmap import update_heatmap, show_heatmap

# Generate fake hit and fail data
def generate_test_data(num_hits=30, num_fails=20, width=800, height=600):
    hits = [(random.randint(100, width - 100), random.randint(100, height - 100)) for _ in range(num_hits)]
    fails = [(random.randint(100, width - 100), random.randint(100, height - 100)) for _ in range(num_fails)]
    return hits, fails

# Main test function
def run_heatmap_test():
    hit_points, fail_points = generate_test_data()
    heatmap = update_heatmap(hit_points, fail_points)
    show_heatmap("Test Fork Heatmap")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_heatmap_test()
