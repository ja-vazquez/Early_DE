
import os

lede = [(3.5, 10.5),(4.5, 9),(5.5,7.5),(6.5,6.5),(7.5,5.5)]#[(5, 10.5)] #, (8.5, 8.5), (8.5, 7.5), (8.5, 6.5), (8.5, 6.)]
#lede = [(8.5, 6.)]

theta_lcdm =1.040911
# 1.041887 
#1.036942

i=1
with open('ede_values.dat','wa') as fede:
 for b, sig in lede:

  count       = 0
  tol, Ttol   = 100, 3e-4
  lowr, highr = 50, 90

  i+=1
  while(abs(tol) > Ttol):
     mid = (lowr + highr)/2.0
  #if True:
  #   mid = 67.6
     
     line  = "hubble         = %f"%(mid)	
     linea = "B             = %f"%(b)
     lineb = "sigma          = %f"%(sig)
     #line2 = "omega_ede      = %f"%(ede)
     line2 = "ede_Da_file = test_ede_Da_0%i.dat"%(i*100)
     line3 = "ede_Om_file = test_ede_Om_%i.dat"%(i*100)
     commd = """
       sed '1i%s\n  2i%s\n 3i%s\n 4i%s\n 5i%s'  params_quint.ini > params1.ini
       ./camb params1.ini > out.txt
     """%(line, linea, lineb,line2, line3)
     os.system(commd)

     with open('out.txt','r') as f:
       for line in f:
	  #print line
          vals =line.split()[0:]
          if '100_theta_' in line:
             theta = float(vals[-1])
	  if 'Om_m' in line:
	     Om = float(vals[-1])
	     print Om
          if 'r_s(zdrag)' in line:
             rs = float(vals[-1])
	  if 'sigma8' in line:
	     s8 = float(vals[-1])
             #break
     
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
