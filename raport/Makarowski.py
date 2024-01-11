import numpy as np
import matplotlib.pyplot as plt

# Dane wejściowe
masa_pocisku = 50  # kg
wysokosc_pocisku = 100  # m
predkosc_pocisku = 60  # m/s
przyspieszenie_grawitacyjne = 9.81  # m/s^2
k_oporu_powietrza = 5  # Stała oporu powietrza

# Funkcja opisująca równanie ruchu z siłą oporu powietrza
def rownanie_ruchu(v, t):
    return przyspieszenie_grawitacyjne - (k_oporu_powietrza / masa_pocisku) * v

# Metoda Eulera do rozwiązania równania różniczkowego
def metoda_eulera(h, czas_symulacji):
    v = predkosc_pocisku
    t = 0
    wysokosc = wysokosc_pocisku
    czas = [t]
    predkosc = [v]
    wysokosci = [wysokosc]

    while t < czas_symulacji and wysokosc >= 0:
        v = v + h * rownanie_ruchu(v, t)
        wysokosc = wysokosc + h * v
        t = t + h

        czas.append(t)
        predkosc.append(v)
        wysokosci.append(max(wysokosc, 0))  # Nie spuszczamy się poniżej poziomu ziemi

    return czas, predkosc, wysokosci

# Parametry symulacji
krok_czasowy = 0.01
czas_symulacji = 100

# Wywołanie funkcji do obliczeń
czas, predkosc, wysokosci = metoda_eulera(krok_czasowy, czas_symulacji)

# Wysokość maksymalna
wysokosc_maksymalna = max(wysokosci)

# Prędkość uderzenia o grunt
predkosc_uderzenia = predkosc[-1]

# Wykresy
plt.plot(czas, wysokosci)
plt.title('Wysokość w funkcji czasu')
plt.xlabel('Czas [s]')
plt.ylabel('Wysokość [m]')
plt.show()

# Wyniki
print(f'Wysokość maksymalna: {wysokosc_maksymalna:.2f} m')
print(f'Prędkość uderzenia o grunt: {predkosc_uderzenia:.2f} m/s')
