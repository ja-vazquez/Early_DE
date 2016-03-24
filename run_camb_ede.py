
import os

lede = [0.00, 0.02, 0.04, 0.06, 0.08]
theta_lcdm = 1.041887
#1.036942


with open('ede_values.dat','wa') as fede:
 for ede in lede:

   count       = 0
   tol, Ttol   = 100, 1e-6
   lowr, highr = 65, 75


   while(abs(tol) > Ttol):
     mid = (lowr + highr)/2.0
     h0 = mid

     line  = "hubble         = %f"%(mid)
     line2 = "omega_ede      = %f"%(ede)
     line3 = "ede_file = test_Da_0%i.dat"%(ede*100)
     commd = """
        sed '1i%s\n 2i%s\n 3i%s'  params.ini > params1.ini
        ./camb params1.ini > out.txt
     """%(line, line2, line3)
     os.system(commd)

     with open('out.txt','r') as f:
        for line in f:
	   #print line
	   vals =line.split()[0:]
	 
	   #if 'r_s(zstar)' in line:
	   #  rs = float(vals[2]) 
	   if '100*theta' in line:
	     theta = float(vals[2])
	   #  break
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


