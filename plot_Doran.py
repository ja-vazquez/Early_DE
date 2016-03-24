import pylab
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

dir = '/astro/u/jvazquez/BOSS/cosmomc_july_14/camb/'




if False:
 names = ['ede_02','ede_04','ede_06','ede_08']
 lnames = len(names)
 lnat, Oedet = [], []
 for name in names:
    pnames=open(dir+name+'.dat').readlines()
    lpnames = len(pnames)
    lna, Oede0 = [], []
    for l in range(lpnames):
        vals =pnames[l].split()[0:]
	lna.append(float(vals[0]))
  	Oede0.append(float(vals[1]))      

    zipped = zip(lna, Oede0)
    s = sorted(zipped, key=lambda x: x[0])

    lna2, Oede2 = [], []
    for l in range(lpnames):
        if (l % 10):
           lna2.append(s[l][0])
           Oede2.append(s[l][1]) 
    lnat.append(lna2)
    Oedet.append(Oede2)
    print 'Hiiii'

if False:
 fig =pylab.figure(figsize=(6,5))
 ax = fig.add_subplot(1,1,1)
 for i in range(lnames):
  ax.plot(lnat[i], Oedet[i])   
 pylab.xscale('log')
 plt.xlim(xmin=1.0e-5)
 plt.show()




da_names = ['test_Da_00','test_Da_02','test_Da_04','test_Da_06','test_Da_08']

rss, ede, h0 = [], [], []
f =open(dir + 'ede_values.dat').readlines()
for l in range(len(f)):
  vals = f[l].split()[0:]
  ede.append(float(vals[0]))
  h0.append(float(vals[1]))
  rss.append(float(vals[2]))

lnames = len(da_names)
ede_rs = [1 - rss[i]/(1- nede)**(0.5)/rss[0] for i, nede in enumerate(ede)]
#ede_rs = [rss[0]*(1- nede)**(0.5)/rss[i] for i, nede in enumerate(ede)]


print ede, ede_rs
pnames=open(dir+'test_Da_00'+'.dat').readlines()
lpnames = len(pnames)
Da_lcdm, Dh_lcdm = [], []
for l in range(lpnames):
   vals =pnames[l].split()[0:]
   Da_lcdm.append(float(vals[1]))
   Dh_lcdm.append(float(vals[2]))

lnat, dat, dht = [], [], []
j=0
for name in da_names:
    pnames=open(dir+name+'.dat').readlines()
    lpnames = len(pnames)
    lna, da, dh = [], [], []
    
    for l in range(lpnames):
        vals =pnames[l].split()[0:]
        lna.append(float(vals[0]))
        da.append((float(vals[1])/rss[j])/(Da_lcdm[l]/rss[0]))
        dh.append((float(vals[2])/rss[j])/(Dh_lcdm[l]/rss[0]))
    lnat.append(lna)
    dat.append(da)
    dht.append(dh) 
    j+=1


#--------
fig =pylab.figure(figsize=(16,5))
ax = fig.add_subplot(1,3,3)
for i in range(lnames):
   ax.plot(lnat[i], dat[i], label='$\Omega_{ede}=%s$'%(ede[i]))
#plt.errorbar(0.57, 1.0045, yerr=0.015)
ax.grid(True)
pylab.xscale('log')
plt.legend(loc = 'upper right')
plt.xlabel("$z$")
plt.ylabel("$[D_A/r_s]_{ede} / [D_A/r_s]_{LCDM}$")
plt.xlim([0.1,10000])
#plt.ylim([0.99,1.01])

ax3 = fig.add_subplot(1,3,2)
for i in range(lnames):
   ax3.plot(lnat[i], dht[i], label='$\Omega_{ede}=%s$'%(ede[i]))
#plt.errorbar(0.57, 1.0045, yerr=0.015)
ax3.grid(True)
pylab.xscale('log')
#plt.legend(loc = 'upper right')
plt.xlabel("$z$")
plt.ylabel("$[D_h/r_s]_{ede} / [D_h/r_s]_{LCDM}$")
plt.xlim([0.1,10000])
#plt.ylim([0.99,1.01])


ax2 = fig.add_subplot(1,3,1)
#ax2.plot(ede, ede_rs)
ax2.grid(True)
sc =ax2.scatter(ede,ede_rs, c=h0, s =40, cmap=cm.Blues, label = 'H0')
cbar = plt.colorbar(sc)
plt.xlabel("$\Omega_{ede}$")
plt.ylabel("$1 - r_{s,ede} / \sqrt{1-\Omega_{ede}} / r_{s,LCDM}$")
plt.xlim([0,0.1])
plt.ylim([-0.003, 0])
cbar.set_label('$H_0$', rotation=270)



fig.tight_layout()
plt.savefig('Doran.pdf')
plt.show()


scals = ['test_ede_00_totCls.dat','test_ede_02_totCls.dat','test_ede_04_totCls.dat',
	'test_ede_06_totCls.dat','test_ede_08_totCls.dat']

clsT, llsT = [], []
for scal in scals:
    pnames=open(dir+scal).readlines()
    lpnames = len(pnames)
    lls, cls = [], []

    for l in range(lpnames):
        vals =pnames[l].split()[0:]
        lls.append(float(vals[0]))
	cls.append(float(vals[1]))
    llsT.append(lls)
    clsT.append(cls)


fig =pylab.figure(figsize=(9,5))
ax = fig.add_subplot(1,1,1)
for i in range(5):
   ax.plot(llsT[i], clsT[i], label='$\Omega_{ede}=%s$'%(ede[i]))
#plt.errorbar(0.57, 1.0045, yerr=0.015)
ax.grid(True)
pylab.xscale('log')
plt.legend(loc = 'upper right')
plt.xlabel("$l$")
plt.ylabel("$Cls$")
plt.xlim([10,2000])

fig.tight_layout()
plt.savefig('Doran_cls2.pdf')
plt.show()
