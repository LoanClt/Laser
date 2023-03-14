import matplotlib.pyplot as plt
import math as m

A21 = 3*10**(6) #s-1
sigmaP = 9.3*10**(-24) #m²
sigma = 3*10**(-23)
longueurOnde = 514*10**(-9) #m
c = 3*10**8 #m.s-1
h = 6.62607015*10**(-34)
frequence = c/longueurOnde #s-1
rayon = 50*10**(-6) #m
surface = m.pi*rayon**2

N = 50

def deltaNsurN(I, puissancePompage):
    intensitePompage = puissancePompage / (surface * h * frequence)
    return sigmaP*intensitePompage/(A21 + sigma*I + sigmaP*intensitePompage)

Y = []
Z = []
W = []
X = []

for i in range(1, N):
    I = 10**i
    X.append(m.log(I))
    Y.append(deltaNsurN(I, 1))
    Z.append(deltaNsurN(I, 10))
    W.append(deltaNsurN(I, 100))

plt.plot(X, Y, label="P = 1W")
plt.plot(X, Z, label="P = 10W")
plt.plot(X, W, label="P = 100W")
plt.xlabel("log(I)")
plt.legend()
plt.ylabel("DeltaN/N")
plt.show()
