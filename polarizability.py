import numpy as np
from drude_model import dielectric_function

def polarizability(radius, wavelength, epsilon_medium):

    radius = radius * 1e-9

    epsilon = dielectric_function(wavelength)

    alpha = 4*np.pi*(radius**3) * (epsilon-epsilon_medium)/(epsilon+2*epsilon_medium)

    return alpha