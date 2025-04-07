from live_fork_hud import simulate_live_trail, generate_dynamic_fork, render_fork_hud

x, y, z = simulate_live_trail()
fy, fz, glow = generate_dynamic_fork(x, y, z)
render_fork_hud(x, y, z, fy, fz, glow)