import matplotlib.pyplot as plt
import project_functions as pf

"""
mu_list contains a sample of 3 mu parameters to plot. x0 and v0 are the initial
amplitude and velocity.

The graphs shown on the essay are for:
    
mu_list = [0.1, 1, 10] & x0, v0 = 0.01, 0   or x0, v0 = 3, 1 (fig.1-2)    

mu_list = [-0.1, -1, -10] & x0, v0 = 0.01, 0   (fig. 6-7)    

tf is the final time, at which the ODE solver will stop.
h is the imposed time interval.
"""
mu_list = [0.1, 1, 10] #mu values
x0, v0 = 0.01, 0

tf = 180
h = 0.01

"""
a for loop calculates the phase and time evolution of the VdP Oscillator for 
the imposed initial conditions and for the 3 different requested mu values.
The sol variable contains all the data of interest, which is then expressed in:
-t: the time values considered when calculating the evolution of the system;
-x: the VdP amplitude value, calculated as a function of t;
-v: the velocity of the system, calculated as a function of t.

The retrieved arrays are then plotted. portrait contains all the subplots
of amplitude over time, and is hence used to visualise the time evolution,
while portrait2 contains the subplots of the velocity over amplitude, hence
visualising the phase evolution.
"""

#phase plots for different initial positions and mu:
portrait = fig,(ax1, ax2, ax3) = plt.subplots(3, 1, figsize = (12, 10))
ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax1.set(ylabel = "displacement(x)", title = "Time evolutions of the VdP Oscillator")
ax2.set(ylabel = "displacement (x)" )
ax3.set(xlabel="time (t)", ylabel = "displacement (x)" )

portrait2 = fig2,(ax4, ax5, ax6) = plt.subplots(1, 3, figsize = (12, 6))
ax4.grid(True)
ax5.grid(True)
ax6.grid(True)
ax4.set(ylabel = "velocity (v)", xlabel = "displacement (x)" )
ax5.set(xlabel = "displacement (x)" )
ax6.set(xlabel = "displacement (x)" )

fig2.suptitle("phase plots of the VdP Oscillator")

#the loop allows us to plot the phase portraits 
#for both x0 = 1 m and x0 = 3 m
j = 0
for i in mu_list:
    mu = i
    sol = pf.RK4(x0, v0, tf, h, pf.VdP, mu) #tf = 30 s
    t, x, v = sol[0], sol[1], sol[2]
    portrait[1][j].plot(t, x, label ="$\mu$ = {0}".format(i))
    portrait2[1][j].plot(x, v, label ="$\mu$ = {0}".format(i))
    j += 1
 
fig2.tight_layout()       
ax1.legend(loc = "best")
ax2.legend(loc = "best")
ax3.legend(loc = "best")
ax4.legend(loc = "best")
ax5.legend(loc = "best")
ax6.legend(loc = "best")