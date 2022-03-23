import matplotlib.pyplot as plt
import project_functions as pf

mu_list = [-0.1, -1, -10] #mu values
x0, v0 = 0.01, 0

tf = 180
h = 0.01

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