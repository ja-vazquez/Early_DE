
#!/usr/bin/env python
import pylab
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import matplotlib.cm as cm
import os, sys, time
import pandas as pd

dir = '/Users/josevazquezgonzalez/Desktop/work/Papers/Joint_Lya_BAO/Quint/Early_DE/data/quint/'
file_values = 'ede_values.dat'
file_Oede   = 'test_ede_Om_200.dat'

rs_lcdm = 147.42
z_cmb = np.log(1./(1+1060.0))

val = pd.read_table(dir + file_values, names =['B','lambda','H0','rs','s8','Om'])


Oede_values = pd.read_fwf(dir + file_Oede, names = ['loga', 'Oede'])
interp_Oede = interp1d(Oede_values['loga'], Oede_values['Oede'])



print interp_Oede(z_cmb), 1.0 - (val['rs'][0]/rs_lcdm)*(1.0 - interp_Oede(z_cmb) )**(-0.5)
