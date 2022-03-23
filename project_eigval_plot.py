import numpy as np
import matplotlib.pyplot as plt

## eigenvalues plot

def eigvals(mu):
    mu = complex(mu)
    lambda_1 = mu/2 + np.sqrt((mu/2)**2 -1) 
    lambda_2 = mu/2 - np.sqrt((mu/2)**2 -1)
    return(lambda_1, lambda_2)


mu_list = np.linspace(-4, 4, 100)

R1, I1, R2, I2 = [], [], [], []
for x in mu_list:
    eigval1, eigval2 = eigvals(x)
    Real_1, Im_1 = np.real(eigval1), np.imag(eigval1)
    Real_2, Im_2 = np.real(eigval2), np.imag(eigval2)
    R1 = np.append(R1, Real_1)
    I1 = np.append(I1, Im_1)
    R2 = np.append(R2, Real_2)
    I2 = np.append(I2, Im_2)

fig,(ax1, ax2) = plt.subplots(1, 2, figsize = (9, 3.75))
ax1.plot(mu_list, R1, label = "$\lambda_+$")
ax1.plot(mu_list, R2, label = "$\lambda_-$")
ax2.plot(mu_list, I1, label = "$\lambda_+$")
ax2.plot(mu_list, I2, label = "$\lambda_-$")
ax1.set(title = "Real part of Eigenvalues")
ax2.set(title = "Imaginary part of Eigenvalues")
ax1.set(xlabel="$\mu$ parameter", ylabel = "Real part" )
ax2.set(xlabel="$\mu$ parameter", ylabel = "Imaginary part" )
ax1.grid(True)
ax2.grid(True)
ax1.legend()
ax2.legend()
fig.tight_layout()