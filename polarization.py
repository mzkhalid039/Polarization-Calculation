
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Prompt user to input lattice parameters
a = float(input("Enter lattice vector A: "))
b = float(input("Enter lattice vector B: "))
c = float(input("Enter lattice vector C: "))

# Read in atomic coordinates from input files
with open('POSCAR', 'r') as f:
    lines = f.readlines()
    pos_atoms = np.array([list(map(float, line.split()[:3])) for line in lines[8:]])

with open('CONTCAR', 'r') as f:
    lines = f.readlines()
    cont_atoms = np.array([list(map(float, line.split()[:3])) for line in lines[8:]])

with open('Born.txt', 'r') as f:
    born_data = np.loadtxt(f)

# Calculate differences in fractional coordinates for each axis, taking into account periodic boundary conditions
dx = cont_atoms[:, 0] - pos_atoms[:, 0]
dy = cont_atoms[:, 1] - pos_atoms[:, 1]
dz = cont_atoms[:, 2] - pos_atoms[:, 2]

dx = np.where(dx > 0.9, (dx - 1) * a, dx * a)
dy = np.where(dy > 0.9, (dy - 1) * b, dy * b)
dz = np.where(dz > 0.9, (dz - 1) * c, dz * c)

dx -= np.round(dx)
dy -= np.round(dy)
dz -= np.round(dz)

# Write differences to file
with open('difference.txt', 'w') as f:
    for i in range(len(dx)):
        f.write(f"{dx[i]:.6f} {dy[i]:.6f} {dz[i]:.6f}\n")

# Plot contour plots of differences along each axis
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))
im1 = ax1.tricontourf(pos_atoms[:, 1], pos_atoms[:, 2], dx, cmap='rainbow', levels=500)
im2 = ax2.tricontourf(pos_atoms[:, 0], pos_atoms[:, 2], dy, cmap='rainbow', levels=500)
im3 = ax3.tricontourf(pos_atoms[:, 0], pos_atoms[:, 1], dz, cmap='rainbow', levels=500)

# Set plot labels and titles
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('dx')

ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('dy')

ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_title('dz')

# Add a colorbar
divider = make_axes_locatable(ax3)
cax = divider.append_axes("right", size="5%", pad=0.05)
cbar = plt.colorbar(im3, cax=cax)
cbar.set_label('Difference')

plt.tight_layout()
plt.show()

# Read dipole_moment.txt file and calculate polarization
diff_data = np.loadtxt('difference.txt')
dipole_moment = np.multiply(diff_data[:, :3], born_data[:, :3])
polarization = np.sum(dipole_moment, axis=0) / (a * b * c)  # divide by cell volume to get polarization

# Save polarization array to file and print output
np.savetxt('polarization.txt', polarization)
print("Final polarization along x-axis: ", polarization[0])
print("Final polarization along y-axis: ", polarization[1])
print("Final polarization along z-axis: ", polarization[2])

