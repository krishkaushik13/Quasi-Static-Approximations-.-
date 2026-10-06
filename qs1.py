import numpy as np
#from constants import n_medium
from drude_model import dielectric_function
n_medium = 1.33
def polarizability_qs1(radius, wavelength):

    radius_m = radius * 1e-9
    wavelength_m = wavelength * 1e-9

    eps = dielectric_function(wavelength)

    eps_m = n_medium**2

    V = (4/3) * np.pi * (radius_m**3)

    x = (2*np.pi*n_medium*radius_m) / wavelength_m

    alpha = (
        (3*V*(eps-eps_m))
        /
        (
            eps
            +2*eps_m
            -(eps-eps_m)*(x**2)
            -1j*(eps-eps_m)*(2/3)*(x**3)
        )
    )

    return alpha


##def cross_sections_qs1(radius, wavelength):

    wavelength_m = wavelength * 1e-9

    alpha = polarizability_qs1(
        radius,
        wavelength
    )

    k = (2*np.pi*n_medium) / wavelength_m

    extinction = k*np.imag(alpha)

    scattering = (k**4/(6*np.pi))*np.abs(alpha)**2

    absorption = extinction - scattering

    return absorption, scattering, extinction##