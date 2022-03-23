# essay_ph456
code for the essay project for the PH456 class.

- project_functions.py: The following file contains the main functions used for this essay, namely the Runge-Kutta 4 routine for the numerical calculation of the time evolutions, and the Van Der Pol Oscillator function. 
- project_eigval_plot.py: As the eigenvalues of the Jacobian discussed in the essay are analytically derived, their behaviour is plotted as a function of the parameter \mu. As the solutions can be complex, both the Real and Imaginary components are shown.
- time_evol_phase_plot.py: the following script plots the time evolution and phase plot of the VdP Oscillator for a given value of \mu. It also plots the behaviour of the system under Liénard's transformation by describing y as a function of x, with y and x defined as in the essay.
- project_multiplot.py: contains a routine where different subplots are graphed, each showing the time evolution of the system for a given array of \mu. A second set of subplots is also plotted for the same array of \mu, this time showcasing the phase plots of the system.
