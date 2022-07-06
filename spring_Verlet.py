import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
m = 1
k = 1
x = 0
v = 1

# simulation time, timestep and time
t_max = 100
dt = 1.0
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
x_list = []
v_list = []
counter = 0

# Verlet Integration
for t in t_array:
    # append current state to trajectories
    x_list.append(x)
    v_list.append(v)
    counter += 1

    # calculate new position and velocity
    a = -k * x / m
    if counter < 2:
        x = x + dt * v
        v = v + dt * a

    else:
        x = 2*x_list[counter-1] - x_list[counter-2] + (dt**2)*a
        v = (1/dt)*(x-x_list[counter-1])

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)
v_array = np.array(v_list)


# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x_array, label='x (m)')
plt.plot(t_array, v_array, label='v (m/s)')
plt.legend()
plt.show()

print('The critical dt value is:', dt, 's')