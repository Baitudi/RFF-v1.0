
import cv2
import numpy as np

def analyze_fork_convergence(forks):
    convergence_map = {}
    for fork in forks:
        end = tuple(fork["end"])
        convergence_map[end] = convergence_map.get(end, 0) + 1
    return convergence_map

def draw_convergence_overlay(frame, convergence_map, threshold=2):
    for point, count in convergence_map.items():
        if count >= threshold:
            radius = 5 + (count * 2)
            intensity = min(255, count * 40)
            color = (0, intensity, 255)
            cv2.circle(frame, point, radius, color, -1)
    return frame
