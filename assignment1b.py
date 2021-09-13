import numpy as np
import matplotlib.pyplot as plt
data= np.loadtxt('cabauw_2019.dat', unpack = True)

nr = data[1-1,:]
day = data[2-1,:]
month = data[3-1,:]
year = data[4-1,:]
julian_day = data[5-1,:]
psurf = data[6-1,:]
u_200 = data[7-1,:]
u_140 = data[8-1,:]
u_80 = data[9-1,:]
u_40 = data[10-1,:]
u_20 = data[11-1,:]
u_10 = data[12-1,:]
v_200 = data[13-1,:]
v_140 = data[14-1,:]
v_80 = data[15-1,:]
v_40 = data[16-1,:]
v_20 = data[17-1,:]
v_10 = data[18-1,:]
Temp_200 = data[19-1,:]
Temp_140 = data[20-1,:]
Temp_80 = data[21-1,:]
Temp_40 = data[22-1,:]
Temp_20 = data[23-1,:]
Temp_10 = data[24-1,:]
Temp_2 = data[25-1,:]
qv_200 = data[26-1,:]
qv_140 = data[27-1,:]
qv_80 = data[28-1,:]
qv_40 = data[29-1,:]
qv_20 = data[30-1,:]
qv_10 = data[31-1,:]
qv_2 = data[32-1,:]
SHF = data[33-1,:]
LHF = data[34-1,:]
LW_up = data[35-1,:]
LW_dn = data[36-1,:]
SW_up = data[37-1,:]
SW_dn = data[38-1,:]
theta = data[39-1,:]

#2a Compute the annual mean values of the upward and downward solar and in- frared
#radiative fluxes1. Compute the ground surface albedo from the annual mean 
#upward and downward solar radiative fluxes.
print('2a')
LHF_clean=LHF
LHF_clean = LHF_clean[LHF_clean != -9999.0]
LW_up_clean=LW_up
LW_up_clean = LW_up_clean[LW_up_clean != -9999.0]
LW_dn_clean=LW_dn
LW_dn_clean = LW_dn_clean[LW_dn_clean != -9999.0]
SW_up_clean=SW_up
SW_up_clean = SW_up_clean[SW_up_clean != -9999.0]
SW_dn_clean=SW_dn
SW_dn_clean = SW_dn_clean[SW_dn_clean != -9999.0]

LW_up_mean=np.mean(LW_up)
print("Avearge infra upward is ", LW_up_mean)
LW_dn_mean=np.mean(LW_dn)
print("Avearge infra downward is ", LW_dn_mean)
SW_up_mean=np.mean(SW_up)
SW_dn_mean=np.mean(SW_dn)
albedo=SW_up_mean/SW_dn_mean
print("Albedo is ", albedo)

#2b. (10 points) The data file gives the solar zenith angle θ. 
#This enables to compute the shortwave radiative flux received 
#at the top of the atmosphere at the location of Cabauw by SW↓TOA = S0 cos θ.

#(i.) Compute the annual mean value of SW↓TOA and compare its value to the 
#annual mean upward and downward infrared radiative fluxes at the ground surface. 
#Which downward flux is larger?
#(ii.) Calculate the total effect of absorption and reflection of solar radiation 
#by the atmosphere by computing the difference between the downward solar radiative 
#fluxes at the TOA and the observed value at the ground surface.

##???? theta calculation
#SWTOA_dn=SW_dn*np.cos(theta/360*2*np.pi)
print('2b')
So=1361
SWTOA_dn=So*np.cos(theta/360*2*np.pi)
SWTOA_dn_mean=np.mean(SWTOA_dn)
print("SWTOA downwards on averrge is ", SWTOA_dn_mean, "W/m^2")
print(SWTOA_dn_mean-SW_dn_mean,"W/m^2 is absorbed/reflected")
print(1-SW_dn_mean/SWTOA_dn_mean,"% is absorbed/reflected")

## 2c.(10 points) (i.)  Make a scatter plot of the observed shortwave radiative  uxes
## at the surfaceas a function of the solar zenith angle.  Choose the size of 
##your dots small enough to enable a distinction between the different measurement 
##points.The maximum values represent conditions with clear (cloud free) skies. 
## The maximum valuesare not falling on a smooth line because the fraction of the 
##solar radiation that is re ected andabsorbed depends on the amounts of aerosols 
##and water vapor, both of which are highly variablein time and space.  Also some 
##patches of thin high clouds may be present.  Let us express theclear sky downward 
##solar radiative  ux at the ground surface asSW#sfc;clr=S0cosexp(=cos)(2)
##(ii.)  Find a best estimate for the clear sky optical depth
##by making a  t by eye.  Add this result,as well as the downward solar radiation 
##received at the top of the atmosphere to your scatter plot.(iii.)  Compute the annual 
##mean value of the downward surface shortwave radiation SW#sfc;clrunder the assumption 
##that at any time clear skies prevail.  With this result we are in a positionto estimate 
##the mean cloud e ect on solar radiation.  To this end compute the di erence betweenthe 
##annual mean values of SW#sfc;clrand the observed downward surface shortwave radiation.
##How large is this cloud radiative forcing e ect for Cabauw?
print('2c')
tau=0.25
plt.scatter(theta, SW_dn, s=0.05)
plt.plot(theta, SWTOA_dn)
plt.legend(['SWTOA'])
plt.xlabel('Theta [degree]')
plt.ylabel('Short Radiation adiation flux [Wm^-2]')
plt.title('Zenith angle against wavelength')

## 2d) The sensible heat flux (SHF) is the energy flux that is used to heat the atmosphere 
#and the latent heat flux (LHF) is the evaporation flux in units of Wm−2 (note that 
#∼29 Wm−2 represents an evaporation rate of about 1 mm/day).
#Compute the annual mean values of the SHF and LHF. Which one is the largest? 
#Hypothesize how the ratio SHF/LHF will change in desert areas like the Sahara. 
#Briefly discuss the seasonal variation of the evaporation.
print('2d')
    
data_clean=data
#rows with LHF=-9999
error_LHF_indx= np.where(LHF == -9999.0)
error_SHF_indx= np.where(SHF == -9999.0)
error_idx=np.hstack((error_LHF_indx,error_SHF_indx))[0]
data_clean=np.delete(data_clean, error_idx, 1)
SHF_clean = data_clean[33-1,:]
LHF_clean = data_clean[34-1,:]
print(np.mean(SHF_clean),"is the average SHF")
print(np.mean(LHF_clean),"is the average LHF")

##2e.(10 points) The websitehttps://www.worlddata.info/europe/netherlands/energy-co
##nsumption.phppresents the total energy consumption of the Netherlands.(i.)   Convert 
##the  total  energy  consumption  to  Watts  and  normalize  this  number  by  the 
##totalpopulation of the Netherlands.(ii.)  Now assume that one will use photovoltaic 
##panels (PVs) with an eciency of 10% to producethe total amount of energy consumed 
##in the Netherlands.  ComputeAand`if the total surfacearea occupied by PVs isA=`2.
print('2e')
Total_Energy_consumption =108.80 *10**9 *10**3
Total_population=1728*10**4
energyperperson=Total_Energy_consumption/Total_population
print('per person energy watts', energyperperson)

efficiency=0.1

A=Total_Energy_consumption/(SW_dn_mean*efficiency)
print('Area in m^2',A)
l=A**(1/2)
print('l in m',l)

