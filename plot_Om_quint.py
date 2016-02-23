
#!/usr/bin/env python
import pylab
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import matplotlib.cm as cm
import os, sys, time

dir = '/gpfs01/astro/workarea/jvazquez/cosmomc_Quint/camb/'

params1 = {'backend': 'pdf',
               'axes.labelsize': 16,
               'text.fontsize': 18,
               'xtick.labelsize': 18,
               'ytick.labelsize': 18,
               'legend.draw_frame': False,
               'legend.fontsize': 12,
               'lines.markersize': 6,
               'font.size': 18,
               'text.usetex': True}#
pylab.rcParams.update(params1)


def colour(x):
    if x==1: return 'red'
    if x==2: return 'blue'
    if x==3: return 'black'
    if x==4: return 'magenta'
    if x==5: return 'cyan'
    if x==6: return 'orange'
    if x==7: return 'green'
    if x==8: return 'yellow'
    if x==9: return 'purple'
    if x>9: return 'black' # print("Increased colouring")

root = 'test_'

names = ['test_ede_Om_200.dat','test_ede_Om_300.dat','test_ede_Om_400.dat','test_ede_Om_500.dat','test_ede_Om_600.dat'] 


zLOWZ  = 0.32
zCMASS = 0.57
zLyaA  = 2.34-0.06
zLyaC  = 2.36+0.06

z_CMB = 1090.43
rd_EHtoCAMB =153.19/149.281


rs,  h0, s8, Om0 =  [], [], [], []
f =open(dir + 'ede_values.dat').readlines()
for l in range(len(f)):
  vals = f[l].split()[0:]
  h0.append(float(vals[2]))
  rs.append(float(vals[3]))
  s8.append(float(vals[4]))
  Om0.append(float(vals[5]))

rs_lcdm = 147.42 
s=0
lnat, Omt, Oedet, Oedet0, inter_Oede = [], [], [], [], []
for name in names:
  pnames=open(dir+name).readlines()
  lpnames = len(pnames)
  lna, Om, Oede, Oede0 = [], [], [], []  
  for l in range(lpnames):
     if ((l< lpnames/3.) or (l> lpnames/3. and l%50 == 0)):      
       vals =pnames[l].split()[0:]
       lna.append(float(vals[0])) 
       Oede0.append(float(vals[1]))	
       Oede.append((1. - float(vals[1]))**(-0.5))
       Om.append(float(rs[s])*(1. - float(vals[1]))**(-0.5)/rs_lcdm)     
  lnat.append(lna)
  Omt.append(Om)
  Oedet.append(Oede)
  Oedet0.append(Oede0)
  s+=1

inter_Oede0_0 = interp1d(lnat[0], Oedet0[0])
inter_Oede_0 = interp1d(lnat[0], Oedet[0])
inter_Oede0_1 = interp1d(lnat[1], Oedet0[1])
inter_Oede_1 = interp1d(lnat[1], Oedet[1])
inter_Oede0_2 = interp1d(lnat[2], Oedet0[2])
inter_Oede_2 = interp1d(lnat[2], Oedet[2])
inter_Oede0_3 = interp1d(lnat[3], Oedet0[3])
inter_Oede_3 = interp1d(lnat[3], Oedet[3])
inter_Oede0_4 = interp1d(lnat[4], Oedet0[4])
inter_Oede_4 = interp1d(lnat[4], Oedet[4])


pnames=open(dir+'test_ede_Da_lcdm.dat').readlines()
lpnames = len(pnames)
Da_lcdm, Dh_lcdm = [], []

for l in range(lpnames): 
   vals =pnames[l].split()[0:]
   Da_lcdm.append(float(vals[1]))
   Dh_lcdm.append(float(vals[2]))


namesq = ['test_ede_Da_0200.dat','test_ede_Da_0300.dat','test_ede_Da_0400.dat','test_ede_Da_0500.dat','test_ede_Da_0600.dat']
lnaat, Dat, Dht = [], [], []
s=0
for name in namesq:
    pnames=open(dir+name).readlines()
    lpnames = len(pnames)
    lnaa, Da, Dh = [], [], []
    print lpnames, len(Da_lcdm)
    for l in range(lpnames):
       vals =pnames[l].split()[0:]
       lnaa.append(float(vals[0]))  
       Da.append((float(vals[1]))/(Da_lcdm[l])) 
       Dh.append((float(vals[2]))/(Dh_lcdm[l]))
    s+=1       

    lnaat.append(lnaa)
    Dat.append(Da) 
    Dht.append(Dh)

inter_Da_0 = interp1d(lnaat[0], Dat[0])
inter_Dh_0 = interp1d(lnaat[0], Dht[0])
inter_Da_1 = interp1d(lnaat[1], Dat[1])
inter_Dh_1 = interp1d(lnaat[1], Dht[1])
inter_Da_2 = interp1d(lnaat[2], Dat[2])
inter_Dh_2 = interp1d(lnaat[2], Dht[2])
inter_Da_3 = interp1d(lnaat[3], Dat[3])
inter_Dh_3 = interp1d(lnaat[3], Dht[3])
inter_Da_4 = interp1d(lnaat[4], Dat[4])
inter_Dh_4 = interp1d(lnaat[4], Dht[4])



ar = np.log(1./(1+1060.0))
nn0, nn1, nn2, nn3, nn4, nn5 = [], [], [], [], [], []
for i in range(0,len(names)):
   n0 = 'inter_Oede0_%i(ar)'%(i)
   n1 = 'inter_Oede_%i(ar)'%(i) 
   #n2 = 'inter_Da_%i(ar)'%(i)
   #n3 = 'inter_Dh_%i(ar)'%(i)
   #n4 = 'inter_Da_%i(ar)'%(i)
   #n5 = '(1+0.41*inter_Oede0_%i(ar))/(1-0.1*inter_Oede0_%i(ar))'%(i, i)

   nn0.append(eval(n0))
   nn1.append(1.0 - eval(n1)*float(rs[i])/rs_lcdm)
   #nn2.append(eval(n1)*eval(n2))
   #nn3.append(eval(n1)*eval(n3))
   #nn4.append(eval(n4)*rs_lcdm/float(rs[i]))
   #nn5.append(eval(n5))

   #print nn0, nn1, nn2  
#-------------------------------------

if True:
 fig =pylab.figure(figsize=(16,12))

# ax = fig.add_subplot(1,3,1)
# for i in range(0,len(names)):
#     ax.plot(lnat[i], Oedet0[i], color=colour(i+1), label = "$r_s$ =%3.2f,"%(float(rs[i])))
# #ax.plot([ar,ar],[0,0.8])
# ax.grid(True)
# plt.legend(loc="upper left")
# #plt.ylim([0,0.8])
# plt.xlim([-14,0])
# plt.xlabel("$\ln a$")
# plt.ylabel("$\Omega_{ede}$")

# ax2 = fig.add_subplot(2,3,4)
# for i in range(0,len(names)):
#    ax2.plot(lnat[i],Omt[i],color=colour(i+1))
# ax2.grid(True)
# #plt.xlim([-14,0])
# #plt.ylim(ymax=1.2)
# #plt.ylim([0.9,1.2])
# plt.xlabel("$\ln a$")
# plt.ylabel("$[r_{s,ede}~/~\sqrt{1-\Omega_{ede}}]~/~r_{s,LCDM}$")

 ax3 = fig.add_subplot(2,3,1)
 for i in range(0,len(namesq)):
     #nameO = 'inter_Oede_%i(lnaat[%i])'%(i,i)
     ax3.plot(lnaat[i], np.array(Dat[i])*(rs_lcdm/float(rs[i])),color=colour(i+1),label = '$\Omega_{ede} = $%1.3f'%(nn0[i]))   
 pylab.xscale('log')
 ax3.plot([0.01,10000], [1,1], 'k-')
 plt.legend(loc="lower right")
 plt.xlim([0.1,10000])
 ax3.grid(True)
 plt.errorbar(zCMASS, 1.044/rd_EHtoCAMB , yerr= 0.015)
 plt.errorbar(zLyaA, 0.973,  yerr= 0.055)
 plt.errorbar(zLyaC, 0.93,   yerr= 0.036)
 #plt.errorbar(z_CMB,  1,            yerr=0.00032)

 plt.xlabel("$z$")
 plt.ylabel("$[D_{A,ede}/r_{s,ede}]/[D_{A,LCDM}/r_{s,LCDM}]$") 

 ax2 = fig.add_subplot(2,3,2)
 for i in range(0,len(namesq)):
     #print i
     #nameO = 'inter_Oede_%i(lnaat[%i])'%(i,i)
     ax2.plot(lnaat[i], np.array(Dht[i])*(rs_lcdm/float(rs[i])),color=colour(i+1))
 ax2.plot([0.01,10000], [1,1], 'k-')
 pylab.xscale('log')
 plt.errorbar(zCMASS, 0.968,     yerr=0.033) 
 plt.errorbar(zLyaA,  1.054,       yerr=0.032)
 plt.errorbar(zLyaC,  1.04,        yerr=0.034)

 plt.xlim([0.1,10000])
 ax2.grid(True)
 #plt.errorbar(0.57, 1.0144, yerr=0.0098)
 #plt.errorbar(2.35, 0.973, yerr=0.05)
 plt.xlabel("$z$")
 plt.ylabel("$[D_{h,ede}/r_{s,ede}]/[D_{h,LCDM}/r_{s,LCDM}]$")


 ax4 = fig.add_subplot(2,3,4)
 #ax4.plot(nn0, nn1)
 sc =ax4.scatter(nn0, nn1, c=h0, s =40, cmap=cm.Blues, label = 'H0')
 cbar = plt.colorbar(sc)
 cbar.set_label('$H_0$')
 ax4.grid(True)
 plt.xticks(np.arange(0.01, 0.08, 0.02))
 plt.xlabel("$ \Omega_{ede}(z_{drag})$")
 plt.ylabel("$1 - r_{s,ede}~/~\sqrt{1-\Omega_{ede}}~/~r_{s,LCDM}$")


 ax5 = fig.add_subplot(2,3,5)
 #ax4.plot(nn0, nn1)
 sc =ax5.scatter(nn0, s8, c=Om0, s =40, cmap=cm.Blues, label = 'Om0')
 cbar = plt.colorbar(sc)
 cbar.set_label('$\Omega_{m,0}$')
 ax5.grid(True)
 plt.xticks(np.arange(0.01, 0.08, 0.02))
 plt.xlabel("$ \Omega_{ede}(z_{drag})$")
 plt.ylabel("$\sigma_8$")

 ax6 = fig.add_subplot(2,3,6)
 #ax4.plot(nn0, nn1)
 sc =ax6.scatter(Om0, s8, c=h0, s =40, cmap=cm.Blues, label = 'h0')
 cbar = plt.colorbar(sc)
 cbar.set_label('$H_0$')
 ax6.grid(True)
 plt.xticks(np.arange(0.2, 0.3, 0.02))
 plt.xlabel("$\Omega_{m,0}$")
 plt.ylabel("$\sigma_8$")

# ax5 = fig.add_subplot(3,3,8)
# ax5.plot(nn0, nn2)
# ax5.grid(True)
# plt.xlabel("$\Omega_{ede}(z_{drag})$")
# plt.ylabel("$[D_{A,ede}~/~\sqrt{1-\Omega_{ede}}]~/~D_{A,LCDM} (z_{drag})$")

# ax6 = fig.add_subplot(3,3,9)
# ax6.plot(nn0, nn3)
# ax6.grid(True)
# plt.xlabel("$\Omega_{ede}(z_{drag})$")
# plt.ylabel("$[D_{H,ede}~/~\sqrt{1-\Omega_{ede}}]~/~D_{H,LCDM} (z_{drag})$")

# ax5 = fig.add_subplot(1,3,3)
# for i in range(0,len(namesq)):
#    ax7.plot(lnaat[i],np.array(Dht[i])*(rs_lcdm/float(rs[i])),color=colour(i+1))
##        label = "$r_s$ =%3.2f,"%(float(rs[i])))
## plt.legend(loc="lower right")
# ax7.grid(True)
 #plt.xlabel("$\ln a$")
 #plt.ylabel("$[D_H/r_s]_{ede}~/~[D_H/r_s]_{LCDM}$")


 plt.tight_layout()
 plt.savefig('Dh_Da.pdf')
 plt.show()


#fig =pylab.figure(figsize=(6,5))
#ax = fig.add_subplot(1,1,1)
#ax.plot(nn0, nn4, label = '$[D_A/r_s]~/~[D_A/r_s]_{lcdm}$')
#ax.plot(nn0, nn5, label = '$\sim \sqrt{1+\Omega_{ede}}$')
#plt.xlabel("$\Omega_{ede}(z_{drag})$")
#plt.legend(loc="upper left")
##plt.ylabel("$[D_A/r_s]~/~[D_A/r_s]_{lcdm}$") #/~\sqrt{1+\Omega_{ede}}$")
#plt.tight_layout()
#plt.savefig('Final'+".pdf")
#plt.show()


#if False: 
# ax2 = fig.add_subplot(1,3,2)
# for i in range(0,len(namesq)):
#    ax2.plot(lnaat[i],np.array(Dat[i])*(rs_lcdm/float(rs[i])),color=colour(i+1))
# ax2.grid(True)
# plt.xlabel("$\ln a$")
# plt.ylabel("$[D_A/r_s]_{ede}~/~[D_A/r_s]_{LCDM}$")


# ax3 = fig.add_subplot(1,3,3)
# for i in range(0,len(namesq)):
#    ax3.plot(lnaat[i],np.array(Dht[i])*(rs_lcdm/float(rs[i])),color=colour(i+1),
#	label = "$r_s$ =%3.2f,"%(float(rs[i])))
# plt.legend(loc="lower right")
# ax3.grid(True)
# plt.xlabel("$\ln a$")
# plt.ylabel("$[D_H/r_s]_{ede}~/~[D_H/r_s]_{LCDM}$")


# plt.tight_layout()
# plt.savefig('Dh_Da'+".pdf")
# plt.show()

