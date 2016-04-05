#!/usr/bin/env python
#based on http://arxiv.org/pdf/0906.0396.pdf
# or http://arxiv.org/pdf/gr-qc/9711068v2.pdf
#Scalar Field potential V=V0*exp[-lam*\phi]

from RunBase import *
from scipy import *
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
from scipy.interpolate import interp1d
from matplotlib import gridspec
import pylab, sys
import scipy.optimize as optimize

name = 'Quint_vB'


pts, pts2, pts3, pts4 =[], [], [], []

T=QuintCosmology_try()

lna = np.linspace(-30., 5, 300)
lam_, V0_ = lam_par, V0_par
A_, lB_   = A_par, lB_par

lam_f, V0_f = 4., 1.0 
A_f, B_f   = 0.5, 25.


def ini_phi(xx):
     return (T.Pot(xx,1)**2/T.Pot(xx,0)/4. - T.Pot(xx,0))*exp(-140)*4.E4*(3/2.36) - 1. 



if True:
   lam_.setValue(lam_f)
   A_.setValue(A_f)
   lB_.setValue(B_f) 
   V0_.setValue(V0_f)

   T.updateParams([lam_, V0_, A_, lB_])
  
   sol = T.Ini_phi()
   xx, yy = sol.T
 
   pts.append(T.O_phi(lna))
   pts3.append(T.w_ede(lna)) 
   
   #print 'sol',ini_phi(-4.6)
   #print 'sol', (optimize.bisect(ini_phi, -10, 10))
      
 
if True:
   fig = plt.figure(figsize=(14,10))
   ax=fig.add_subplot(2,3,1)
   ax.plot(lna, pts[0])
   plt.ylim([-0.01,1.01])
   plt.xlim(xmin=-42)
   plt.xlabel("$\ln a$")
   plt.ylabel("$O_{ede}$")
   ax.grid(True)
   
   ax2=fig.add_subplot(2,3,2)
   ax2.plot(lna, pts3[0])
   plt.ylim(ymin=-1.01)
   plt.xlim(xmin=-42)
   plt.xlabel("$\ln a$")
   plt.ylabel("$w$")
   ax2.grid(True)

   ax3=fig.add_subplot(2,3,3)
   ax3.plot(lna, xx)
   plt.xlabel("$\ln a$")
   plt.ylabel("$\phi$")
   ax3.grid(True)

   ax4=fig.add_subplot(2,3,4)
   ax4.plot(lna, yy**2)
   plt.xlabel("$\ln a$")
   plt.ylabel("$\dot \phi^2$")
   pylab.yscale('log')
   ax4.grid(True)

   ax5=fig.add_subplot(2,3,5)
   ax5.plot(lna, T.Pot(xx,0))
   plt.xlabel("$\ln a$")
   plt.ylabel("$V(\phi)$")
   pylab.yscale('log') 
   ax5.grid(True)

   #ax6=fig.add_subplot(2,3,6)
   #ax6.plot(xx, (T.Pot(xx,1)**2/T.Pot(xx,0)/4. - T.Pot(xx,0))*exp(-140)*4.E4*(3/2.36))
   #plt.xlim([-35,-30])   
   #plt.xlabel("$\ln a$")
   #plt.ylabel("$V,{\phi}(\phi)$")
   #pylab.yscale('log')
   #ax6.grid(True)
   plt.show()
