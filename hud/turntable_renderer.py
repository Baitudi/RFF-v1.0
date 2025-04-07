import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import sin, cos, pi

# Optional Flywheel curve import if implemented
try:
    from flywheel_curve_engine import draw_flywheel_curve
except ImportError:
    def draw_flywheel_curve():
        pass  # Placeholder if curve engine is not yet active

def draw_grid():
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_LINES)
    for i in range(-10, 11):
        glVertex3f(i, 0, -10)
        glVertex3f(i, 0, 10)
        glVertex3f(-10, 0, i)
        glVertex3f(10, 0, i)
    glEnd()

def draw_trail():
    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(2)
    glBegin(GL_LINE_STRIP)
    for i in range(100):
        x = (i - 50) / 10.0
        y = sin(i * 0.1) * 0.2
        z = cos(i * 0.1) * 0.4
        glVertex3f(x, y, z)
    glEnd()

def main():
    pygame.init()
    display = (1000, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("RFF Tactical HUD Turntable")

    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, -1.5, -12)
    rot_y, rot_x = 0, 25

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]: rot_y -= 1
        if keys[K_RIGHT]: rot_y += 1
        if keys[K_UP]: rot_x -= 1
        if keys[K_DOWN]: rot_x += 1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(rot_x, 1, 0, 0)
        glRotatef(rot_y, 0, 1, 0)

        draw_grid()
        draw_trail()
        draw_flywheel_curve()

        glPopMatrix()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
