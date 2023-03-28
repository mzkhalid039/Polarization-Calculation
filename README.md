# Polarization-Born-charges
This code reads in input files POSCAR, CONTCAR, and Born.txt from the same directory, prompts the user to input lattice parameters, calculates the differences in fractional coordinates for each axis (taking into account periodic boundary conditions), plots the contour plots of differences along each axis, calculates the dipole moment, and finally calculates the polarization along x, y, and z-axis in unit of uC/cm2. This code uses this formula to calculate the macroscopic polarization:

P^{(i)} = \frac{e}{\Omega_c} \sum_{\alpha}\omega_{\alpha}Z_{\alpha}^* \mu_{\alpha}^{(i)}

Here e is the electron charge, $\Omega_c$ is the volume of the bulk unit-cell $i$, $\mu_{\alpha}$ (CONTCAR) is the displacement of atom $\alpha$ (POSCAR) from the high-symmtry position, $\omega_{\alpha}$ is the number of atoms of that type. The $Z_{\alpha}^*$ are the Born effective charge tensor, which is calculated by the density functional perturbation theory. 

## Requirements
This script requires the following packages to be installed: - `numpy` - `matplotlib`

## Usage 
To run the script, navigate to the directory containing `script.py` and run the following command:

python script.py poscar_path contcar_path born_path [--a A_VAL --b B_VAL --c C_VAL --v V_VAL --conv CONV_VAL]
