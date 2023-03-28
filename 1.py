import matplotlib.pyplot as plt

import math as m

import numpy as np

A21 = 3 * 10 ** (6)  # s-1

sigmaP = 9.3 * 10 ** (-24)  # m²

sigma = 3 * 10 ** (-23)

longueurOnde = 514 * 10 ** (-9)  # m

c = 3 * 10 ** 8  # m.s-1

h = 6.62607015 * 10 ** (-34)

frequence = c / longueurOnde  # s-1

rayon = (50 / 2) * 10 ** (-6)  # m

surface = m.pi * rayon ** 2  # m²


def deltaNsurN(I, puissancePompage):
    intensitePompage = puissancePompage / (surface * h * frequence)

    return sigmaP * intensitePompage / (A21 + sigma * I + sigmaP * intensitePompage)


Y = []

Z = []

W = []

X = np.logspace(1, 50, 10000, base=10)

Y = deltaNsurN(X, 1)

Z = deltaNsurN(X, 10)

W = deltaNsurN(X, 100)

plt.plot(np.log(X), Y, label=r"$P_p = 1$W")

plt.plot(np.log(X), Z, label=r"$P_p = 10$W")

plt.plot(np.log(X), W, label=r"$P_p = 100$W")

plt.xlabel("log(I)")

plt.legend()

plt.ylabel(r"$\frac{\Delta n}{n_t}$")

plt.xlim(60, 75)
