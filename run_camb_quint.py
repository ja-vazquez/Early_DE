
import os

#lede = [ (3.5, 10.5) ,(4.5, 9), (5.5,7.5), (6.5,6.5), (7.5,5.5)]
#amp = [1.98, 1.93, 1.86, 1.78, 1.66, 1.99]

lede = [(5, 9),  (5.5, 8), (6.5, 7), (7.5,6.5)]
amp = [2.05, 2.03, 2.0, 1.99]

#(4.5, 10), 20.5

theta_lcdm = 1.039973

i=1
with open('test_quint_values.dat','wa') as fede:
 for b, sig in lede:

  count       = 0
  tol, Ttol   = 100, 2e-4
  lowr, highr = 50, 100

  i+=1
  while(abs(tol) > Ttol):
     mid = (lowr + highr)/2.0
     line  = "hubble         = %f"%(mid)
     line0 = "#omch2         = %f"%(0.2617605*mid*mid/10000.)	
     line01= "#ombh2          = %f"%(0.141559 - 0.2617605*mid*mid/10000.)
     linea = "B             = %f"%(b)
     lineb = "sigma          = %f"%(sig)
     line2 = "ede_Da_file = test_quint_Da_%i.dat"%(i)
     line3 = "ede_Om_file = test_quint_Om_%i.dat"%(i)
     line4 = "output_root = test_quint_%i"%(i)
     line5 = "scalar_amp(1)             = %fe-9"%(amp[0]) #i-2])
     commd = """
       sed '1i%s\n 2i%s\n 3i%s\n 4i%s\n 5i%s\n 6i%s\n 7i%s\n 8i%s\n 9i%s'  params_quint.ini > params_%i.ini
       ./camb params_%i.ini > out.txt
     """%(line, line0, line01, linea, lineb,line2, line3, line4, line5, i, i)
     os.system(commd)
     os.system("cp out.txt out_%i.tx"%(i))
     with open('out.txt','r') as f:
       for line in f:
          vals =line.split()[0:]
          if '100*theta2' in line:
             theta = float(vals[-1])
	  if 'Om_m' in line:
	     Om = float(vals[-1])
          if 'r_s(zdrag)/Mpc' in line:
             rs = float(vals[-1])
	  if 'sigma8' in line:
	     s8 = float(vals[-1])
     
     print mid, tol
  
     tol = theta - theta_lcdm
     if(abs(tol) < Ttol):
       print 'reach tolerance:',tol, mid
       break
     else:
       if(tol<0):
         lowr = mid
       else:
         highr = mid
     count+=1
     if (count > 15):
       print 'No solution found!'
       break
   
  fede.write("%f\t %f\t %f\t %f\t %f\t %f \n"%(b, sig, mid, rs, s8, Om))
