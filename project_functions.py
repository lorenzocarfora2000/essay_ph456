import numpy as np


def RK4(x0, v0,  tf, h, dvdt, val):
    
    #list of t, with t0 at initial pos.
    t = [0]
    
    #list of x(t) , with x0 at initial pos.
    xpos = [x0] 
    
    #list of v(t) = x’(t), with v0 in initial pos.
    v = [v0] 
    
    while t[-1]<tf:
        
        k1_v = h*dvdt(t[-1], xpos[-1], v[-1], val)
        k1_x = h*v[-1]
        k2_v = h*dvdt(t[-1]+h/2 , xpos[-1]+k1_x/2, v[-1]+k1_v/2 , val)
        k2_x = h*(v[-1]+k1_v/2)
        k3_v = h*dvdt(t[-1]+h/2 , xpos[-1]+k2_x/2, v[-1]+k2_v/2, val )
        k3_x = h*(v[-1]+k2_v/2)
        k4_v = h*dvdt(t[-1]+h, xpos[-1]+k3_x, v[-1]+k3_v, val )
        k4_x =h*(v[-1]+k3_v)
        
        #new v and pos vals
        v_new = v[-1]+k1_v/6 + k2_v/3 + k3_v/3 + k4_v/6
        x_new = xpos[-1]+k1_x/6 + k2_x/3 + k3_x/3 + k4_x/6
        
        #the next step in t, x(t) and v(t) are attached in the arrays:
        t = np.append(t, t[-1]+h)
        v = np.append(v, v_new)
        xpos = np.append(xpos, x_new)
    return t, xpos, v

def VdP(t, x, v, mu):
    return mu*(1-x**2)*v - x 

      