# -*- coding: utf-8 -*-
"""
1a. This year the exoplanet TOI 700d has been discovered.  It orbits the star TOI 700 at
a distanceof 2.4384810e10m.  The star has a radius of 2.9246410e8m and a temperature of
3480 K. Wewill investigate some features of the planet with the global energy balance model
"""
import numpy as np
import matplotlib.pyplot as plt
radius_orbit=2.43848*10**10; #m
radius_star=2.92464*10**8; #m
Temerature_Kelvin_star=3480; #Kelvin

sigma=5.67*10**(-8)
"""
1a.(10 points) Assume that the planet has no atmosphere and a zero surface albedo.
(i.)  Compute the solar constant for the planet.
(ii.)  Compute the mean surface temperature of the planet.
(iii.)  Plot the solar radiation received at the top of the atmosphere as a function 
of wavelength(the Planck function).  Also plot in the same  figure the radiation emitted 
by the planet.  Whatare the values of the wavelengths of the spectral peaks
"""

#i
Solar_constant=(radius_star/radius_orbit)**2*sigma*(Temerature_Kelvin_star**4);#Solar Constant
print("The answer to qustion 1(i) Solar constant (W/m**2) is ", Solar_constant)

#ii
Temperature_Kelvin_planet=(Solar_constant/(4*sigma))**(1/4)
print("The answer to qustion 1(ii) Temperture (Kelvin) is ", Temperature_Kelvin_planet)

# iii
#wrong
#additional constant
c=3*10**8; #light speed(m)
h=6.625*10**(-34); #Planck constant
k=1.38*10**(-23); #Boltzmann constant
#wavelength=np.arange(0,60,0.01);#0 to 2.1 um

Scale=radius_star**2/(radius_star+radius_orbit)**2;
wavelength=np.linspace(0.01,50,num=5999);
wavelength=wavelength*10**(-6);
Radiation_flux_planet=((2*np.pi*h*c**2)/(wavelength**5))*(1/(np.exp(h*c/(k*Temperature_Kelvin_planet*wavelength))-1));
Radiation_flux_star=((2*np.pi*h*c**2)/(wavelength**5))*(1/(np.exp(h*c/(k*Temerature_Kelvin_star*wavelength))-1))*Scale;

plt.plot(wavelength,Radiation_flux_planet*wavelength, 'r');
plt.plot(wavelength,Radiation_flux_star*wavelength, 'b');

#plt.scatter(Radiation_flux_planet.argmax(axis=0)*10**(-8),np.max(Radiation_flux),s=70,c='k')
#plt.scatter(Radiation_flux_star.argmax(axis=0)*10**(-8),np.max(Radiation_flux),s=70,c='k')
plt.xlabel('wavelength (m)')
plt.ylabel('Radiation flux I')
plt.title('Red line: absorbed, Blue line emitted')
plt.show()

"""
1b. This year the exoplanet TOI 700d has been discovered.  It orbits the star TOI 700 at
a distanceof 2.4384810e10m.  The star has a radius of 2.9246410e8m and a temperature of
3480 K. Wewill investigate some features of the planet with the global energy balance model
"""