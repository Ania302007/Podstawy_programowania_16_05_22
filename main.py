import matplotlib.pyplot as plt
import numpy
import numpy as np

rng = np.random.default_rng()
K=np.linspace(1,10,10)
print(K)
N=1000
a=0
b=1
m=12
def rozklad(a, b, N):
    dist = rng.uniform(a, b, N)

    return dist

def histogram(f1,K):
    hist,bins=np.histogram(f1,K)

    return hist

def suma_rozkładów(f2,m,K):
    sum_of_hist = np.zeros((m,K))
    for _ in range(m):
        sum_of_hist=np.vstack(f2)
    return sum_of_hist
f1=rozklad(a,b,N)
f2=histogram(f1,K)

print(suma_rozkładów(f2,m,K))

# print(histogram(rozklad(a,b,N),K))




#
#
