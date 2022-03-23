import matplotlib.pyplot as plt
import project_functions as pf
import numpy as np

mu = 10             #damping parameter
x0, v0 = 0.01, 0

#RK4 Solver Van Der Pol Equation Solutions:
h = 0.01 #timestep
tf = 60  #final time
sol = pf.RK4(x0, v0, tf, h, pf.VdP, mu) #tf = 10 s
t, x, v = sol[0], sol[1], sol[2]

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