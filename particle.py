import numpy as np
import matplotlib.pyplot as plt
from pressure import *

time = 10
N = 1000
dt = time / (N - 1)
angle = .0873
area_density = 1


def constant_acceleration(M, angle):
    return 0.5

def calc_acceleration(M, angle):
    return area_density * (p_below(M, angle) - p_above(M, angle))

def v_verlet_step(dt, x, v, a, a_func, M, angle):
    v_halfstep = v + 0.5 * a * dt
    x_step = x + v_halfstep * dt
    a_step = a_func(M, angle)
    v_step = v + 0.5 * (a + a_step) * dt
    return x_step, v_step, a_step

positions = np.zeros((2, N), dtype=float)
velocities = np.zeros((2, N), dtype=float)
accelerations = np.zeros((2, N), dtype=float)
velocities[0, 0] = 1.3
accelerations[0, 0] = constant_acceleration(velocities[0, 0], angle)
accelerations[1, 0] = calc_acceleration(velocities[0, 0], angle)

for i in range(N - 1):
    xip1, vip1, aip1 = v_verlet_step(
        dt,
        positions[1, i],
        velocities[1, i],
        accelerations[1, i],
        calc_acceleration,
        velocities[0, i],
        angle
    )

    positions[1, i + 1] = xip1
    velocities[1, i + 1] = vip1
    accelerations[1, i + 1] = aip1

    xip1, vip1, aip1 = v_verlet_step(
        dt,
        positions[0, i],
        velocities[0, i],
        0,#accelerations[0, i],
        constant_acceleration,
        velocities[0, i],
        angle
    )

    positions[0, i + 1] = xip1
    velocities[0, i + 1] = vip1
    accelerations[0, i + 1] = aip1

plt.plot(positions[0,:], positions[1,:])
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Aerofoil Position")
plt.show()
