import matplotlib.pyplot as plt
import project_functions as pf
import numpy as np

"""
The following routine is used to plot the time evolution and phase plot of the
VdP Oscillator for an imposed mu parameter, while x0 & v0 are the initial 
amplitude and velocity respectively. The routine also returns what is defined 
as a Liénard plot, which returns the resulting phase plot of the system 
described with a Liénard transformation. The essay also refers to such plot as
an x-y plot, as y is defined here as the variable used to imposed the Liénard 
transform.
The values imposed for the graphs in the essay are:
    
mu =  10 & x0, v0 = 0.01, 0 (Fig.3)

mu = 0, x0, v0 = 1, 0 (Fig. 5)   

tf is the final time, at which the ODE solver will stop.
h is the imposed time interval.

The sol variable contains all the ODE solutions, which are then expressed as:
-t: the time values considered when calculating the evolution of the system;
-x: the VdP amplitude value, calculated as a function of t;
-v: the velocity of the system, calculated as a function of t.

"""

mu = 1             #damping parameter
x0, v0 = 1, 0

#RK4 Solver Van Der Pol Equation Solutions:
h = 0.01 #timestep
tf = 60  #final time
sol = pf.RK4(x0, v0, tf, h, pf.VdP, mu) #tf = 10 s
t, x, v = sol[0], sol[1], sol[2]


"""
the time evolution and phase plot are graphed as subplots, easing the 
comparison.
"""
#plot comparison
fig,(ax1, ax2) = plt.subplots(1, 2, figsize = (12, 5))
ax1.plot(t, x)
ax2.plot(x, v)
ax1.set(title = "RKF45 - Analytical comparison ($\mu$ = {})".format(mu))
ax2.set(title = "Corresponding phase plot")
ax1.set(xlabel="time t (s)", ylabel = "displacement x (m)" )
ax2.set(xlabel="Displacement x (m)", ylabel = "velocity (m/s)" )
ax1.grid(True)
ax2.grid(True)
fig.tight_layout()

"""
Liénard's transformation is applied by definition, retrieving the y_Lienard
parameter. The x-y plot is also graphed alongside the cubic y = x-(x^3)/3. The
cubic is calculated for a x range cubic_x, derived from the extension of the 
x data, and the y axis data is calculated and stored as cubic_y.
"""

#Using Lienard's picture: 
y_Lienard = x- (x**3)/3 - v/mu 
cubic_x = np.linspace(min(x), max(x), 200)
cubic_y = cubic_x- cubic_x**3/3

plt.figure(3)
plt.plot(x, y_Lienard, label = "VdP Oscillator")
plt.plot(cubic_x, cubic_y, "--", label = "cubic $f(x)$")
plt.grid()
plt.legend(bbox_to_anchor=(1, 1))
plt.xlabel("displacement (x)")
plt.ylabel("Liénard transform (y)")
plt.title("VdP Oscillator under Liénard's transformation, $\mu$ = {}".format(mu))