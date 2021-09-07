import numpy as np
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

#i) Compute the annual mean values of the upward and downward solar and in- frared
#radiative fluxes1. Compute the ground surface albedo from the annual mean 
#upward and downward solar radiative fluxes.
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
#for i in range(1:np.size(LW_up)):
#    if LW_up_clean
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
SWTOA=SW_dn*np.cos(90/360*2*np.pi)

