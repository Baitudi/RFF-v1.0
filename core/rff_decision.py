def generate_prediction_forks(current_position, trail, chart_image):
    """
    Returns fake prediction forks radiating from player_position.
    Replace with real AI logic later.
    """
    if current_position is None:
        return []

    x, y = current_position

    forks = [
        {'start': (x, y), 'end': (x + 80, y - 40), 'confidence': 0.9},
        {'start': (x, y), 'end': (x + 80, y), 'confidence': 0.6},
        {'start': (x, y), 'end': (x + 80, y + 40), 'confidence': 0.3}
    ]
    return forks
