import numpy as np

def generate_forecast_path(start_price, steps=30, trend_strength=0.2, volatility=0.15, drag_factor=0.98, anchors=[]):
    """
    Generates a forecast path with volatility, drag, and anchor influence.

    Parameters:
    - start_price: float
    - steps: int, number of forecast steps
    - trend_strength: float, base momentum per step
    - volatility: float, randomness factor
    - drag_factor: float, decay of momentum
    - anchors: list of macro influence corrections (optional)

    Returns:
    - list of forecasted price points
    """
    path = []
    current_price = start_price
    momentum = trend_strength

    for i in range(steps):
        # Apply anchor correction if available
        anchor_adj = anchors[i] if i < len(anchors) else 0

        # Add volatility and drag
        drift = momentum * drag_factor
        noise = np.random.normal(0, volatility)
        next_price = current_price + drift + noise + anchor_adj

        path.append(next_price)
        current_price = next_price
        momentum *= drag_factor  # reduce over time

    return path
