import numpy as np
from qs1 import polarizability_qs1
from drude_model import dielectric_function
from cross_section_qs1 import cross_sections_qs1
#from cross_sections import extinction
from plot import plot_spectrum


from drude_model import dielectric_function

wavelength = np.linspace(300, 1200, 900)  # Wavelength range in nm

radii_list = [10,20,30,40,50]  # Radii in nm             
      # Mediums (e.g., Air, Water, Glass)


absorption_data = {}
scattering_data = {}
extinction_data = {}
normalized_extinction_data = {}

for radius in radii_list:
   # for n_medium in index_list:
        
        absorption = []
        scattering = []
        extinction_total = []
        normalized_extinction = []
        
        for lam in wavelength:
          a,s,e ,q = cross_sections_qs1(radius, lam )
            
          absorption.append(a)
          scattering.append(s)
          extinction_total.append(e)
          normalized_extinction.append(q)
       
        combo_key = radius
        absorption_data[combo_key] = absorption
        scattering_data[combo_key] = scattering
        extinction_data[combo_key] = extinction_total
        normalized_extinction_data[radius] = normalized_extinction


plot_spectrum(wavelength, absorption_data, scattering_data, extinction_data,normalized_extinction_data)