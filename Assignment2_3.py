import numpy as np
import matplotlib.pyplot as plt
w_data= np.loadtxt('w_field.dat', unpack = True)
T_data= np.loadtxt('T_field.dat', unpack = True)
qt_data= np.loadtxt('qt_field.dat', unpack = True)

w_mean=np.mean(w_data)
T_mean=np.mean(T_data)
qt_mean=np.mean(qt_data)

plt.figure()
CT=plt.contour(w_data)
plt.title('Vertical velocity Contour map (m/s)')
plt.clabel(CT, inline=True, fontsize=8)
plt.show()

plt.figure()
CS=plt.contour(T_data)
plt.title('Temrature Contour map (K)')
plt.clabel(CS, inline=True, fontsize=8)
plt.show()

#(3_2)
w_T=np.sum((w_data-w_mean)*(T_data-T_mean))/(64*64)
w_qt=np.sum((w_data-w_mean)*(qt_data-qt_mean))/(64*64)
print('3_2')
print("w'T'=",w_T)
print("w'qt'=",w_qt)

#(3_3)
I_up=np.zeros([64,64])
I_dn=np.ones([64,64])
for i in range(0,64):
    for j in range(0,64):
        if w_data[i,j]>=0:
            I_up[i,j]=1
            I_dn[i,j]=0

w_up=np.sum(I_up*w_data)/np.sum(I_up)
T_up=np.sum(I_up*T_data)/np.sum(I_up)
qt_up=np.sum(I_up*qt_data)/np.sum(I_up)
print('3_3')
print("wup=",w_up)
print("Tup'=",T_up)
print("qt_up'=",qt_up)
print("w_up-w_mean=",w_up-w_mean)
print("Tup-T_mean'=",T_up-T_mean)
print("qt_up-qt_mean'=",qt_up-qt_mean)
w_dn=np.sum(I_dn*w_data)/np.sum(I_dn)
T_dn=np.sum(I_dn*T_data)/np.sum(I_dn)
qt_dn=np.sum(I_dn*qt_data)/np.sum(I_dn)
print("wdn=",w_dn)
print("Tdn'=",T_dn)
print("qt_dn'=",qt_dn)
print("w_dn-w_mean=",w_dn-w_mean)
print("Tdn-T_mean'=",T_dn-T_mean)
print("qt_dn-qt_mean'=",qt_dn-qt_mean)


