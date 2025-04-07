import pygame

# Trail rendering configuration
TRAIL_COLOR = (0, 255, 0)
PLAYER_COLOR = (255, 255, 255)
TRAIL_RADIUS = 4
PLAYER_RADIUS = 6

def draw_trail(screen, trail_points):
    """
    Draws a glowing trail from past movement points.
    :param screen: pygame surface
    :param trail_points: list of (x, y) positions
    """
    for idx, point in enumerate(trail_points):
        if idx < len(trail_points) - 1:
            pygame.draw.line(screen, TRAIL_COLOR, point, trail_points[idx + 1], 2)
        pygame.draw.circle(screen, TRAIL_COLOR, point, TRAIL_RADIUS)

def draw_player(screen, current_position):
    """
    Draws the blinking player dot.
    :param screen: pygame surface
    :param current_position: (x, y) of the player
    """
    pygame.draw.circle(screen, PLAYER_COLOR, current_position, PLAYER_RADIUS)
