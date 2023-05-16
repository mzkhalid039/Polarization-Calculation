# Macroscopic Polarization from Born charges
This code reads in input files POSCAR, CONTCAR, and Born.txt from the same directory, prompts the user to input lattice parameters, calculates the differences in fractional coordinates for each axis (taking into account periodic boundary conditions), plots the contour plots of differences along each axis, calculates the dipole moment, and finally calculates the polarization along x, y, and z-axis in unit of $\micro C/cm^2$. This code uses the following formulation to calculate the macroscopic polarization:

$P^i = \frac{e}{\Omega_c} \sum_{\alpha}\omega_{\alpha}Z_{\alpha}^* \mu_{\alpha}^{(i)}$

Here e is the electron charge, $\Omega_c$ is the volume of the bulk unit-cell $i$, $\mu_{\alpha}$ (CONTCAR) is the displacement of atom $\alpha$ from the high-symmtry position (POSCAR), $\omega_{\alpha}$ is the number of atoms of that type. The $Z_{\alpha}^*$ are the Born effective charge tensor, which is calculated by the density functional perturbation theory. 

## Requirements
This script requires the following packages to be installed: - `numpy` - `matplotlib`

## Usage of [bcpolarization.py](./bcpolarization.py)
1. Place the input files POSCAR, CONTCAR, and Born.txt in the same directory as the Python script. 
2. Type `python polarization.py` to run the script.
3. Follow the on-screen prompt to enter the lattice parameters.
4. The script will plot the contour plots of differences along each axis and print the final polarization values along x, y, and z-axis. 
5. A polarization.txt file containing the polarization values will be created in the same directory as the script. 

## Usage of [pcpolarization.py](./bcpolarization.py)
 Place the input (polar) non-centrosymmtric CONTCAR and (non-polar) centrosymmtric POSCAR files in the same folder as the script. Run the script and it will give a prompt to enter formal charges for the elements. Enter the values and you will get the final polarization values in units of $\micro C/cm^2$. You can find the example of using this script in the [examples](/examples) folder for Rhombohedral $BaTiO_3$, tetragonal $PbTiO_3$ and hexagonal $YMnO_3$. 

 Note: The input files should have the same format as the standard VASP input/output file format. 

## License 
This code is released under the [MIT License](LICENSE).
