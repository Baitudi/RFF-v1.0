from OpenGL.GL import *
from math import sin, cos, pi

# Generate a smooth Bezier-like curve from points

def generate_flywheel_curve():
    curve_points = []
    for t in range(100):
        angle = t * 0.1
        x = sin(angle) * 4 + cos(angle * 0.5)
        y = cos(angle) * 2 + sin(angle * 0.3)
        z = t * 0.12 - 6
        curve_points.append((x, y, z))
    return curve_points


def draw_flywheel_curve():
    glColor3f(1.0, 0.8, 0.2)  # golden curve
    glLineWidth(3)
    glBegin(GL_LINE_STRIP)
    for x, y, z in generate_flywheel_curve():
        glVertex3f(x, y, z)
    glEnd()
