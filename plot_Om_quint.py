
#!/usr/bin/env python
import pylab
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import matplotlib.cm as cm
import os, sys, time
import pandas as pd


def colour(x):
    if x==1: return 'red'
    if x==2: return 'blue'
    if x==3: return 'green'
    if x==4: return 'cyan'
    if x==5: return 'magenta'
    if x==6: return 'black'
    if x==7: return 'green'
    if x==8: return 'yellow'
    if x==9: return 'purple'
    if x>9: return 'black' # print("Increased colouring")

zLOWZ  = 0.32
zCMASS = 0.57
zLyaA  = 2.34-0.06
zLyaC  = 2.36+0.06

z_CMB = 1090.43
rd_EHtoCAMB =153.19/149.281


dir = '/Users/josevazquezgonzalez/Desktop/work/Papers/Joint_Lya_BAO/Quint/Early_DE/data/quint/'
file_values = 'ede_values.dat'
file_Oede   = 'test_ede_Om_'
file_Da     = 'test_ede_Da_'

rs_lcdm = 147.42
z_cmb = np.log(1./(1+1060.0))



#---------------Read Files-------------------#


    #Values file
val = pd.read_table(dir + file_values, names =['B', 'lambda', 'H0', 'rs', 's8', 'Om'])



    #Oede file
one_fact, Oede_cmb = [], []
for i in range(5):
    Oede_values = pd.read_fwf(dir + file_Oede + '%i00.dat'%(i+2), names = ['loga', 'Oede'])
    interp_Oede = interp1d(Oede_values['loga'], Oede_values['Oede'])

    Oede_cmb.append(interp_Oede(z_cmb))
    one_fact.append(1.0 - (val['rs'][i]/rs_lcdm)*(1.0 - interp_Oede(z_cmb) )**(-0.5))



    #Da/Dh files
da, dh = [], []
dist_lcd   = pd.read_fwf(dir + 'test_ede_Da_lcdm.dat', names = ['z', 'da', 'dh'])
for j in range(5):
    dist_vals  = pd.read_fwf(dir + file_Da + '0%i00.dat'%(j+2), names = ['z', 'da', 'dh'])

    da.append((dist_vals['da']/val['rs'][j])/(dist_lcd['da']/rs_lcdm))
    dh.append((dist_vals['dh']/val['rs'][0])/(dist_lcd['dh']/rs_lcdm))




#---------------Plots -------------------#

if True:

 fig = pylab.figure(figsize=(16,12))


 ax3 = fig.add_subplot(2,3,1)
 for i in range(5):
     ax3.plot(dist_lcd['z'], da[i],color=colour(i+1),label = '$\Omega_{ede} = $%1.3f'%(Oede_cmb[i]))
 pylab.xscale('log')
 ax3.plot([0.01,10000], [1,1], 'k-')
 plt.legend(loc="lower right")
 plt.xlim([0.1,1100])
 ax3.grid(True)
 plt.errorbar(zCMASS, 1.044/rd_EHtoCAMB , yerr= 0.015)
 plt.errorbar(zLyaA, 0.973,  yerr= 0.055)
 plt.errorbar(zLyaC, 0.93,   yerr= 0.036)



 ax4 = fig.add_subplot(2,3,4)
 sc = ax4.scatter(Oede_cmb, one_fact, c=val['H0'], s =40, cmap=cm.Blues, label = 'H0')
 cbar = plt.colorbar(sc)
 cbar.set_label('$H_0$', rotation=90)
 ax4.grid(True)
 plt.axis([0.01, 0.09, 0, 0.01])
 plt.xticks(np.arange(0.01, 0.09, 0.02))
 plt.xlabel("$ \Omega_{ede}(z_{drag})$")
 plt.ylabel("$1 - r_{s,ede}/\sqrt{1-\Omega_{ede}}/r_{s,LCDM}$")



 ax5 = fig.add_subplot(2,3,5)
 sc = ax5.scatter(Oede_cmb, val['s8'], c=val['Om'], s =40, cmap=cm.Blues, label = 'Om0')
 cbar = plt.colorbar(sc)
 cbar.set_label('$\Omega_{m,0}$')
 ax5.grid(True)
 plt.axis([0.01, 0.09, 0.82, 0.9])
 plt.xticks(np.arange(0.01, 0.09, 0.02))
 plt.xlabel("$ \Omega_{ede}(z_{drag})$")
 plt.ylabel("$\sigma_8$")



 ax6 = fig.add_subplot(2,3,6)
 sc = ax6.scatter(val['Om'], val['s8'], c=val['H0'], s =40, cmap=cm.Blues, label = 'h0')
 cbar = plt.colorbar(sc)
 cbar.set_label('$H_0$')
 ax6.grid(True)
 plt.xticks(np.arange(0.2, 0.3, 0.02))
 plt.xlabel("$\Omega_{m,0}$")
 plt.ylabel("$\sigma_8$")


 plt.tight_layout()
 plt.show()