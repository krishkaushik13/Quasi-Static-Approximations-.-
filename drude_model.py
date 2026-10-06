import numpy as np
import pandas as pd

data = pd.read_csv("Index_Au_Ag.csv")

wavelength_data = data["Lambda"].values[::-1]
n_data = data["AuRe"].values[::-1]
k_data = data["AuIm"].values[::-1]

def dielectric_function(wavelength):

    n = np.interp(wavelength,
                  wavelength_data,
                  n_data)

    k = np.interp(wavelength,
                  wavelength_data,
                  k_data)

    epsilon = (n + 1j*k)**2

    return epsilon
