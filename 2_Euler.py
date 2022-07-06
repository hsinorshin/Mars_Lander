import numpy as np
import matplotlib.pyplot as plt

''' With the centre of the planet as the origin of the coordinate system, x,y are perpendicular to the direction of the 
position vector of the body and z the altitude of the body. x is in the same direction as the equator '''

# mass, spring constant, initial position and velocity
m = 1
k = 1
x = 0
v = 1

# Mars constant
# mass of mars
M = 6.42E23
# radius of Mars
r = 3386000.0
# gravitational constant
G = 6.67e-11
# height above mars surface
R = 10000
#force exerted on body
F_g = (G*m*M) / ((R+r)**2)

# simulation time, timestep and time
t_max = 100
dt = 0.0001
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
xx_list = []
xy_list = []
xz_list = []
vx_list = []
vy_list = []
vz_list = []

# Euler integration
for t in t_array:

    # append current state to trajectories
    xz_list.append(x)
    vz_list.append(v)

    # calculate new position and velocity
    a = -F_g / m
    x = x + dt * v
    v = v + dt * a
#creating 3xn matrices
position = np.array([[xx_list],[xy_list],[xz_list]])
velocity = np.array([[vx_list], [vy_list], [vz_list]])

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, xz_list, label='x (m)')
plt.plot(t_array, vz_list, label='v (m/s)')
plt.legend()
plt.show()

