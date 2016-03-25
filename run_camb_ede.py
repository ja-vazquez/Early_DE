
import os

lede = [0.00, 0.02, 0.04, 0.06, 0.08]
amp = [2.215, 2.165, 2.118, 2.07, 2.025]
theta_lcdm = 1.041887


i=1
with open('ede_values.dat','wa') as fede:
 for ede in lede:

   count       = 0
   tol, Ttol   = 100, 1e-6
   lowr, highr = 65, 75

   i=2
   while(abs(tol) > Ttol):
     mid = (lowr + highr)/2.0
     h0 = mid

     line  = "hubble         = %f"%(mid)
     line2 = "omega_ede      = %f"%(ede)
     line2b= "scalar_amp(1)  = %fe-9"%(amp[i-2])
     line3 = "ede_file = test_Da_0%i.dat"%(ede*100)
     line4 = "output_root = test_ede_0%i"%(ede*100)
     commd = """
        sed '1i%s\n 2i%s\n 3i%s\n 4i%s\n 5i%s'  params.ini > params1.ini
        ./camb params1.ini > out.txt
     """%(line, line2, line2b, line3, line4)
     os.system(commd)

     with open('out.txt','r') as f:
        for line in f:
	   vals =line.split()[0:]
	 
	   if '100*theta' in line:
	     theta = float(vals[2])
	   if 'r_s(zdrag)' in line:
	     rs = float(vals[2])	
     	     break


     tol = theta - theta_lcdm
     if(abs(tol) < Ttol):  
	print 'reach tolerance:',tol
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
   
   fede.write("%f\t %f\t %f \n"%(ede, mid, rs))


