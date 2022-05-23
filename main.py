import matplotlib.pyplot as plt
import numpy
import numpy as np

rng = np.random.default_rng()

N = 1000
a = 0
b = 1
m = 120
K = np.linspace(start=0, stop=1, num=10)


def rozklad(a, b, N):
    dist = rng.uniform(a, b, N)

    return dist


def histogram(f1, K):
    hist, bins = np.histogram(f1, K)

    return hist


def skladanie_macierzy():
    suma_wierszy = []
    for _ in range(m):
        wiersz = histogram(rozklad(a,b,N),K)
        suma_wierszy.append(wiersz)
    macierz = np.array(suma_wierszy)
    print(macierz)
    return macierz
macierz=skladanie_macierzy()
def średnia(i):
    suma=macierz.sum(axis=0)
    średnia=suma[i]/macierz.shape[0]
    return średnia
def odchylenie(i):
    suma = 0
    for j in range(macierz.shape[0]):
        suma += (macierz[j][i] - średnia(i)) ** 2
    return np.sqrt(suma / (macierz.shape[1] - 1))
def wykresy(f3):
    macierz=f3.transpose()
    il_wierszy=macierz.shape[0]
    # print(il_wierszy)
    fig,axs=plt.subplots(3,3,sharex=True,sharey=True)
    p=0
    q=0
    for i in range(il_wierszy):
        axs[p][q].hist(macierz[i],label="Kolumna" + str(i))
        print(macierz[i].mean())
        axs[p][q].legend(loc='upper right')
        axs[p][q].set_title(f"Średnia {średnia(i):.4} \ns={odchylenie(i):.4}")
        axs[p][q].set(xlabel='wartości', ylabel='ilość wartości')
        if q == 2:
            p += 1
            q = 0
        else:
            q += 1
    plt.show()
wykresy(skladanie_macierzy())