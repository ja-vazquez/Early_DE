
import os

lede = [0.02, 0.04, 0.06, 0.08]
#amp = [2.1] 
amp = [2.145, 2.1, 2.05, 2.005]
theta_lcdm = 1.040930


i=1
with open('test_ede_values.dat','wa') as fede:
 for ede in lede:

   count       = 0
   tol, Ttol   = 100, 1e-6
   lowr, highr = 65, 75

   i+=1
   while(abs(tol) > Ttol):
     mid = (lowr + highr)/2.0
     h0 = mid

     line  = "hubble         = %f"%(mid)
     line2 = "omega_ede      = %f"%(ede)
     line2b= "scalar_amp(1)  = %fe-9"%(amp[i-2])
     line3 = "ede_Da_file = test_ede_Da_%i.dat"%(i)
     line3b = "ede_Om_file = test_ede_Om_%i.dat"%(i)
     line4 = "output_root = test_ede_%i"%(i)
     commd = """
        sed '1i%s\n 2i%s\n 3i%s\n  4i%s\n 5i%s\n 6i%s'  params_ede.ini > params1.ini
        ./camb params1.ini > out.txt
     """%(line, line2, line2b, line3, line3b, line4)
     os.system(commd)

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
     if (count >15):
        print 'No solution found!'
        break
   
   fede.write("%f \t%f \t%f \t%f \t%f \n"%(ede, mid, rs, s8, Om))


