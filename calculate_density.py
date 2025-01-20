###########################################################################################################
#    Script to calculate the density of given cell from [ABC] for Ta2O5                                   
###########################################################################################################

import math

def calculate_density(a, b, c, alpha, beta, gamma, n, molar_mass):
    # Convert angles from degrees to radians
    alpha_rad = math.radians(alpha)
    beta_rad = math.radians(beta)
    gamma_rad = math.radians(gamma)
    
    # Calculate the volume of the unit cell
    volume = a * b * c * math.sqrt(
        1 - math.cos(alpha_rad)**2 - math.cos(beta_rad)**2 - math.cos(gamma_rad)**2
        + 2 * math.cos(alpha_rad) * math.cos(beta_rad) * math.cos(gamma_rad)
    )
    
    # Constants
    avogadro_number = 6.02214076e23  # Avogadro's number in mol^-1
    
    # Calculate density in g/cm^3
    density = (n * molar_mass) / (avogadro_number * volume * 1e-24)
    
    return density

# Example parameters for Ta2O5
a = 12.633017 # in Angstroms
b = 15.179004  # in Angstroms
c = 19.481613  # in Angstroms
alpha = 90  # in degrees
beta = 90  # in degrees
gamma = 90  # in degrees
n = 40  # number of formula units in the unit cell
molar_mass = 441.89  # molar mass of Ta2O5 in g/mol

density = calculate_density(a, b, c, alpha, beta, gamma, n, molar_mass)
print(f"Density of Ta2O5: {density:.4f} g/cm^3")
