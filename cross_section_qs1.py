from drude_model import dielectric_function
from qs1 import polarizability_qs1
import numpy  as np
n_medium = 1.33
def cross_sections_qs1(radius, wavelength):

    wavelength_m = wavelength * 1e-9

    alpha = polarizability_qs1(
        radius,
        wavelength
    )

    radius_m = radius * 1e-9

    geometric_area = np.pi * (radius_m**2)

    
    k = (2*np.pi*n_medium) / wavelength_m

    absorption = k*np.imag(alpha)
    
    scattering = (k**4/(6*np.pi))*(np.abs(alpha**2))

    extinction = absorption + scattering
    Q_ext = extinction / geometric_area
    return absorption, scattering, extinction , Q_ext