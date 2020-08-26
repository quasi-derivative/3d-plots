# Import
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Setup the figure and the subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')    # projection='3d' makes it a 3d plot

# Create the data
X = np.arange(-30.0, 30.0, 0.3)
Y = np.arange(-30.0, 30.0, 0.3)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)    # Finds the radii of concentric circles at the given resolution
Z = np.sin(R) * 0.001*R**2    # The z axis is the sine of R multiplied by a paraboloid (makes the value increase in amlpitude)

# The 3d surface plot
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                       cmap='viridis', linewidth=0, antialiased=False, alpha=1)

# Creates the "projections"
# The function usually creates contours in 3d space. By offsetting to the limit, they look flat
# levels = 0 tells it to only use one slice of the surface, which is the plane along the center
ax.contour(X, Y, Z, levels=0, zdir='z', offset=-10, cmap='viridis')
ax.contour(X, Y, Z, levels=0, zdir='x', offset=-60, cmap='viridis')
ax.contour(X, Y, Z, levels=0, zdir='y', offset=60, cmap='viridis')

# Formatting
ax.set_xlim(-60, 60)
ax.set_ylim(-60, 60)
ax.set_zlim(-10, 10)
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
