import numpy as np
from turntable_renderer import render_turntable
from fork_engine import calculate_dynamic_fork, generate_fixed_forks

# Simulated trail
x = np.linspace(-10, 10, 500)
y = np.sin(x)
z = np.cos(x)

# Generate forks
dynamic_fork = [calculate_dynamic_fork(x, y, z)]
fixed_forks = generate_fixed_forks(x, y, z)

# Combine for display
all_forks = dynamic_fork + fixed_forks

render_turntable(x, y, z, all_forks)
