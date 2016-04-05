
#!/usr/bin/env python
import pylab
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import matplotlib.cm as cm
import pandas as pd
import Useful as Usf


params1 = Usf.setting_plot()
pylab.rcParams.update(params1)

zLOWZ  = 0.32
zCMASS = 0.57
zLyaA  = 2.34-0.06
zLyaC  = 2.36+0.06

z_CMB = 1090.43
rd_EHtoCAMB =153.19/149.281

rs_lcdm = 147.42
lna_cmb = np.log(1./(1+1060.0))

quint = False


file_Cls    = '_scalCls.dat'
file_Mpk    = '_matterpower.dat'

file_cls_lcdm   = 'test_lcdm_scalCls.dat'
file_mpk_lcdm   = 'test_lcdm_matterpower.dat'
file_da_lcdm    = 'test_Da_lcdm.dat'


if quint == True:
   dir = '/Users/josevazquezgonzalez/Desktop/work/Papers/Joint_Lya_BAO/Quint/Early_DE/data/quint/'
   root        = 'test_quint_fix_'
   val = pd.read_table(dir + root + 'values.dat', names =['B', 'lambda', 'H0', 'rs', 's8', 'Om'])
   rr = 5 #num of files

else:
   dir = '/astro/u/jvazquez/BOSS/cosmomc_july_14/camb/'
   root = 'test_ede_'
   val = pd.read_table(dir + root + 'values.dat', names =['Ode', 'H0', 'rs', 's8', 'Om'])
   colspecs=([0,15],[24,37],[45,59])
   rr = 4

file_Oede   = root + 'Om_'
file_Da     = root + 'Da_'



#---------------Read Files----------------------#



    #Oede file
one_fact, Oede_cmb = [], []
lna, Oede, wede = [], [], []
for i in range(rr):
    Oede_values = pd.read_fwf(dir + file_Oede + '%i.dat'%(i+2),  colspecs=colspecs , names = ['loga', 'Oede', 'wde'])
    interp_Oede = interp1d(Oede_values['loga'], Oede_values['Oede'])

    lna.append(Oede_values['loga'])
    Oede.append(Oede_values['Oede'])
    wede.append(Oede_values['wde'])  
    
    Oede_cmb.append(interp_Oede(lna_cmb))
    one_fact.append(1.0 - (val['rs'][i]/rs_lcdm)*(1.0 - interp_Oede(lna_cmb) )**(-0.5))


    #Da/Dh files
da, dh = [], []
dist_lcd   = pd.read_fwf(dir + file_da_lcdm, colspecs = colspecs, names = ['z', 'da', 'dh'])
for j in range(rr):
    dist_vals  = pd.read_fwf(dir + file_Da + '%i.dat'%(j+2), colspecs = colspecs, names = ['z', 'da', 'dh'])
    
    da.append((dist_vals['da']/val['rs'][j])/(dist_lcd['da']/rs_lcdm))
    dh.append((dist_vals['dh']/val['rs'][j])/(dist_lcd['dh']/rs_lcdm))



    #Cls files
cls, ll = [], []
ll = np.loadtxt(dir + file_cls_lcdm, usecols=[0])
cls_lcdm = np.loadtxt(dir + file_cls_lcdm, usecols=[1])
for k in range(rr):
    cls_vals = np.loadtxt(dir + root + '%i'%(k+2) + file_Cls, usecols=[1])
    cls.append(cls_vals/cls_lcdm)



    #Mpk files
mpk, kk= [], []
kk_lcdm = np.loadtxt(dir + file_mpk_lcdm, usecols=[0])
mpk_lcdm = np.loadtxt(dir + file_mpk_lcdm, usecols=[1])

for k in range(rr):
    kk_vals = np.loadtxt(dir + root + '%i'%(k+2) + file_Mpk, usecols=[0])
    mpk_vals = np.loadtxt(dir + root + '%i'%(k+2) + file_Mpk, usecols=[1])

    mpk_interp  = interp1d(kk_vals, mpk_vals)
    mpk.append(mpk_interp(kk_lcdm)/mpk_lcdm)




#---------------Plot Files----------------------#

if True:

 fig = pylab.figure(figsize=(14,11))


 ax4 = fig.add_subplot(3,3,4)
 sc = ax4.scatter(Oede_cmb, one_fact, c=val['H0'], s =40, cmap=cm.Blues, label = 'H0')
 cbar = plt.colorbar(sc)
 cbar.set_label('$H_0$', rotation=90)
 ax4.grid(True)
 if not quint:
 	plt.axis([0.01, 0.09, -0.002, 0.001])
	plt.xticks(np.arange(0.01, 0.09, 0.02))   
 #plt.axis([0.01, 0.09, 0, 0.01])
 #plt.xticks(np.arange(0.01, 0.09, 0.02))
 plt.xlabel("$ \Omega_{ede}(z_{drag})$")
 plt.ylabel("$1 - r_{s,ede}/\sqrt{1-\Omega_{ede}}/r_{s,\Lambda}$")



 ax5 = fig.add_subplot(3,3,5)
 sc = ax5.scatter(Oede_cmb, val['s8'], c=val['Om'], s =40, cmap=cm.Blues, label = 'Om0')
 cbar = plt.colorbar(sc)
 ax5.grid(True)
 cbar.set_label('$\Omega_{m,0}$')
 #plt.axis([0.01, 0.09, 0.8, 0.88])
 plt.xticks(np.arange(0.01, 0.091, 0.02))
 plt.xlabel("$ \Omega_{ede}(z_{drag})$")
 plt.ylabel("$\sigma_8$")



 ax6 = fig.add_subplot(3,3,6)
 sc = ax6.scatter(val['Om'], val['s8'], c=val['H0'], s =40, cmap=cm.Blues, label = 'h0')
 cbar = plt.colorbar(sc)
 ax6.grid(True)
 cbar.set_label('$H_0$')
 if not quint:
	plt.xticks(np.arange(0.29, 0.31, 0.01))
 #plt.xticks(np.arange(0.2, 0.3, 0.04))
 plt.xlabel("$\Omega_{m,0}$")
 plt.ylabel("$\sigma_8$")


 ax1 = fig.add_subplot(3,3,7)
 for i in range(rr):
     ax1.plot(dist_lcd['z'], da[i], color = Usf.colour(i+1),
              label = '$\Omega_{ede} = $%1.3f'%(Oede_cmb[i]))
 ax1.grid(True)
 pylab.xscale('log')
 plt.xlabel("$z$")
 plt.xlim([0.1,1100])
 plt.legend(loc="lower right")
 ax1.plot([0.01,10000], [1,1], 'k-')
 plt.ylabel("$[D_{a,ede}/r_{s,ede}]/[D_{a,\Lambda}/r_{s,\Lambda}]$")
 plt.errorbar(zCMASS, 1.044/rd_EHtoCAMB , yerr= 0.015)
 plt.errorbar(zLyaA, 0.973,  yerr= 0.055)
 plt.errorbar(zLyaC, 0.93,   yerr= 0.036)


 ax2 = fig.add_subplot(3,3,8)
 for i in range(rr):
     ax2.plot(dist_lcd['z'], dh[i], color=Usf.colour(i+1))
 ax2.plot([0.01,10000], [1,1], 'k-')
 ax2.grid(True)
 pylab.xscale('log')
 plt.xlabel("$z$")
 plt.xlim([0.1,1100])
 plt.errorbar(zCMASS, 0.968,     yerr=0.033)
 plt.errorbar(zLyaA,  1.054,       yerr=0.032)
 plt.errorbar(zLyaC,  1.04,        yerr=0.034)
 plt.ylabel("$[D_{h,ede}/r_{s,ede}]/[D_{h,\Lambda}/r_{s,\Lambda}]$")


 ax3 = fig.add_subplot(3,3,9)
 for i in range(rr):
    ax3.plot(ll, cls[i], color=Usf.colour(i+1), label = 'LCDM' if i==5 else None)
 plt.xlim([10,2500])
 #plt.ylim([0.6,1.5])
 ax3.grid(True)
 plt.xlabel("$l$")
 ax3.set_xscale('log')
 plt.ylabel("$CMB_{ede}/CMB_{\Lambda}$")
 plt.legend(loc="upper right")


 #ax7 = fig.add_subplot(3,3,8)
 #for i in range(rr):
 #   ax7.plot(kk_lcdm, mpk[i], color=Usf.colour(i+1)) #, label = 'LCDM' if i==5 else None)
 #ax7.grid(True)
 ##plt.xlim([0.001,1])
 #plt.xlabel("$k$")
 #ax7.set_xscale('log')
 ##ax7.set_yscale('log') 
 #plt.ylabel("$Mpk_{ede}/Mpk_{\Lambda}$")
 #plt.legend(loc="upper right")


 ax8 =  fig.add_subplot(3, 3, 1)
 for i in range(rr):
     z = np.exp(-lna[i])
     ax8.plot(z, Oede[i]) 
 ax8.grid(True) 
 ax8.set_xscale('log') 
 plt.xlabel("$z+1$") 
 plt.ylabel("$\\Omega_{ede}$")
 plt.xlim(xmax = 1.0e6)

 ax9 = fig.add_subplot(3, 3, 2)
 for i in range(rr):
    z = np.exp(-lna[i])
    ax9.plot(z, wede[i])
 ax9.grid(True)
 ax9.set_xscale('log')
 plt.xlabel("$z+1$") 
 plt.ylabel("$w_{ede}$")
 plt.xlim(xmax = 1.0e6)

 plt.tight_layout()
 plt.show()
 plt.savefig(root + 'Om.pdf' )
