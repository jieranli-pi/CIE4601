# -*- coding: utf-8 -*-
"""
1a. This year the exoplanet TOI 700d has been discovered.  It orbits the star TOI 700 at
a distanceof 2.4384810e10m.  The star has a radius of 2.9246410e8m and a temperature of
3480 K. Wewill investigate some features of the planet with the global energy balance model
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

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
wavelength=np.linspace(0.01,120,num=11999);
wavelength=wavelength*10**(-6);
Radiation_flux_planet=((2*np.pi*h*c**2)/(wavelength**5))*(1/(np.exp(h*c/(k*Temperature_Kelvin_planet*wavelength))-1));
Radiation_flux_star=((2*np.pi*h*c**2)/(wavelength**5))*(1/(np.exp(h*c/(k*Temerature_Kelvin_star*wavelength))-1));

plt.plot(wavelength,Radiation_flux_planet*wavelength, 'r', label='from star short wave');
plt.legend(['from star short wave'])
plt.plot(wavelength,Radiation_flux_star*wavelength*Scale/4, 'b', label='from TOI700d infra');
plt.legend()
plt.xscale('log')

peak_wavelength_planet=wavelength[Radiation_flux_planet.argmax(axis=0)];
peak_wavelength_star=wavelength[Radiation_flux_star.argmax(axis=0)];
print("The answer to qustion 1(iii) wavelength peak for star is ", peak_wavelength_planet)
print("The answer to qustion 1(iii) wavelength peak for star is ", peak_wavelength_star)

#plt.scatter(wavelength[Radiation_flux_planet.argmax(axis=0)],np.max(Radiation_flux_planet*wavelength),s=70,c='k')
#plt.scatter(wavelength[Radiation_flux_star.argmax(axis=0)],np.max(Radiation_flux_star),s=70,c='k')
plt.xlabel('wavelength (um)')
plt.ylabel('Radiation flux I * wavelength (W/m^2)')
plt.title('Radiation against wavelength')
plt.show()

"""
1b. This year the exoplanet TOI 700d has been discovered.  It orbits the star TOI 700 at
a distanceof 2.4384810e10m.  The star has a radius of 2.9246410e8m and a temperature of
3480 K. Wewill investigate some features of the planet with the global energy balance model
"""
def func(T):
    e=1
    sigma=5.67*10**(-8)
    alpha=1
    R=0
    So=1196.2073589315598
    return [alpha*sigma*T[0]**4-2*e*sigma*T[1]**4,
            sigma*T[0]**4 -e*sigma*T[1]**4 -(1-R)*So/4]
T = fsolve(func, [1, 1])
print(T)

