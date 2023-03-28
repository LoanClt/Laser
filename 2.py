import matplotlib.pyplot as plt
import math as m
import numpy as np

A21 = 3*10**(6) #s-1
sigmaP = 9.3*10**(-24) #m²
sigma = 3*10**(-23)
longueurOnde = 514*10**(-9) #m
c = 3*10**8 #m.s-1
h = 6.62607015*10**(-34)
frequence = c/longueurOnde #s-1
rayon = 50*10**(-6)/2 #m
surface = m.pi*rayon**2
n = 3*10**25 #m-3

def Qstim(I,puissancePompage):
    intensitePompage = puissancePompage / (surface * h * frequence)
    return sigma*I*((n*sigmaP*intensitePompage)/(A21 + sigma*I + sigmaP*intensitePompage))

def Qspont(I,puissancePompage):
    intensitePompage = puissancePompage / (surface * h * frequence)
    return A21*(n*sigmaP*intensitePompage/(A21 + sigma*I + sigmaP*intensitePompage))

X = np.logspace(1, 40, 10000, base=10)
Yst1 = Qstim(X, 1)
Yst10 = Qstim(X, 10)
Yst100 = Qstim(X, 100)
Ysp1 = Qspont(X, 1)
Ysp10 = Qspont(X, 10)
Ysp100 = Qspont(X, 100)

plt.plot(np.log(X), Yst1, label=r"$Q_{stim} \;\;\; P=1$W")
plt.plot(np.log(X), Yst10, label=r"$Q_{stim} \;\;\; P=10$W")
plt.plot(np.log(X), Yst100, label=r"$Q_{stim} \;\;\; P=100$W")
plt.xlabel(r"$\log(I)$")
plt.plot(np.log(X), Ysp1, label=r"$Q_{spont} \;\;\; P=1$W")
plt.plot(np.log(X), Ysp10, label=r"$Q_{spont} \;\;\; P=10$W")
plt.plot(np.log(X), Ysp100, label=r"$Q_{spont} \;\;\; P=100$W")
plt.legend(loc='upper left')
plt.show()
