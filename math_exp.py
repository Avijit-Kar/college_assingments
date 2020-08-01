#Avijit kumar kar
#fourier transform(1)
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import quad

alpha = 0.5
f0 = lambda x: np.exp(-alpha * (x ** 2))
f1 = lambda x: x * np.exp(-alpha * (x ** 2))


def fourier(f, a, b,):
    return quad(lambda x: np.real(f(x)), a, b)[0] + 1j * quad(lambda x: np.imag(f(x)), a, b)[0]


factor = 1 / np.sqrt(2 * np.pi)
F_T = lambda f: lambda w: factor * fourier(lambda x: f(x) * np.exp(1j * w * x), -np.inf, np.inf)

# graph
range = np.arange(-10, 10, step=0.05)

F0_s = [F_T(f0)(s) for s in range]
F1_s = [F_T(f1)(s) for s in range]

plt.title(r"Fourier Transform of $e^{-\alpha x^2}$")
plt.plot(range, np.real(F0_s), label='real')
plt.plot(range, np.imag(F0_s), label='imaginary')

plt.xlabel(r's $\rightarrow$')
plt.ylabel(r'F(s) $\rightarrow$')
plt.legend()
plt.grid()
plt.show()

plt.title(r"Fourier Transform of $x e^{-\alpha x^2}$")
plt.plot(range, np.real(F1_s), label='real')
plt.plot(range, np.imag(F1_s), label='imaginary')

plt.xlabel(r's $\rightarrow$')
plt.ylabel(r'F(s) $\rightarrow$')
plt.legend()
plt.grid()
plt.show()
