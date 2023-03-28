# Polarization-Born-charges
This code reads in input files POSCAR, CONTCAR, and Born.txt from the same directory, prompts the user to input lattice parameters, calculates the differences in fractional coordinates for each axis (taking into account periodic boundary conditions), plots the contour plots of differences along each axis, calculates the dipole moment, and finally calculates the polarization along x, y, and z-axis in unit of uC/cm2. This code uses this formula to calculate the macroscopic polarization:

$P^i = \frac{e}{\Omega_c} \sum_{\alpha}\omega_{\alpha}Z_{\alpha}^* \mu_{\alpha}^{(i)}$

Here e is the electron charge, $\Omega_c$ is the volume of the bulk unit-cell $i$, $\mu_{\alpha}$ (CONTCAR) is the displacement of atom $\alpha$ (POSCAR) from the high-symmtry position, $\omega_{\alpha}$ is the number of atoms of that type. The $Z_{\alpha}^*$ are the Born effective charge tensor, which is calculated by the density functional perturbation theory. 

## Requirements
This script requires the following packages to be installed: - `numpy` - `matplotlib`

## Usage 
1. Place the input files POSCAR, CONTCAR, and Born.txt in the same directory as the Python script. 
2. Type `python polarization.py` to run the script.
3. Follow the on-screen prompt to enter the lattice parameters.
4. The script will plot the contour plots of differences along each axis and print the final polarization values along x, y, and z-axis. 
5. A polarization.txt file containing the polarization values will be created in the same directory as the script. 

Note: The input files should have the same format as the standard VASP input/output file format. 

## License This code is released under the [MIT License](LICENSE).
