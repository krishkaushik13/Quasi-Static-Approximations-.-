import numpy as np
from polarizability import polarizability

def extinction(radius, wavelength, refractive_index):

    wavelength_m = wavelength * 1e-9

    epsilon_medium = refractive_index**2

    alpha = polarizability(radius,
                           wavelength,
                           epsilon_medium)

    k = 2*np.pi*refractive_index / wavelength_m

    absorption = k * np.imag(alpha)

    scattering = (k**4)/(6*np.pi) * np.abs(alpha)**2

    extinction = absorption + scattering

    return absorption, scattering, extinction