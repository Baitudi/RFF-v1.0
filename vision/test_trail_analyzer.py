from trail_analyzer import calculate_slope_and_velocity, detect_wait_zones

# Simulated trail: a small zigzag movement
test_trail = [
    (100, 200), (105, 200), (110, 202),
    (115, 203), (120, 203), (121, 203)
]

# Analyze slope and velocity
segments = calculate_slope_and_velocity(test_trail)

print("Segment Analysis:")
for seg in segments:
    print(seg)

# Detect wait zones
waits = detect_wait_zones(segments, threshold=2)
print("\nDetected Wait Zones:")
print(waits)
