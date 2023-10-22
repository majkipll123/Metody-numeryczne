# %% [markdown]
# ### Metody numeryczne 1 - Lista 2

# %% [markdown]
# #### Zadanie 1:
# 
# Znajdź, bez używania komputera, reprezentację binarną liczby $1/10$ w 32-bitowym formacie IEEE
# 
# #### Rozwiązanie - na osobnej kartce

# %% [markdown]
# #### Zadanie 2:
# Znajdź najbliższą liczbę maszynową dla 2/7 i błąd względny takiego przybliżenia.
# 
# #### Rozwiązanie - na osobnej kartce

# %% [markdown]
# #### Zadanie 3:
# 
# Napisz program do obliczania dwóch matematycznie równoważnych wyrażeń
# 
# $$\sqrt{x^2+1}-1\$$ 
# 
# i
# 
# $$\frac{x^2}{\sqrt{x^2+1}+1}\,.$$
# 
# Które z nich daje wiarygodne wyniki dla $x=2^{-n}$ i $n=2,\ 4,\ 6,...,\ 24$?
# 
# #### Rozwiązanie:

# %%
import math
import numpy as np

def wzor1(x):
    return (np.sqrt((math.pow(x, 2) + 1)) - 1)
def wzor2(x):
    return ((math.pow(x, 2) / (np.sqrt((math.pow(x, 2) + 1)) + 1)))

for n in range(2, 100, 2):
    x = 2 ** (-n)

    print("x^"+str(n))
    print("Wzor 1:", wzor1(x))
    print("Wzor 2:", wzor2(x), "\n")
    

# %% [markdown]
# #### Zadanie 4:
# 
# Znajdź sposób obliczania wyrażenia
# 
# $$\sqrt{x^2+4}-2$$
# 
# bez straty dokładności.
# 
# #### Rozwiązanie - na osobnej kartce

# %% [markdown]
# #### Zadanie 5:
# 
# Oblicz całki typu
# 
# $$I_n=\int\limits_0^1 x^n e^x\,dx$$
# 
# dla $n=2,\ 3,\ ...,\ 20$, korzystając z rekurencyjnego związku
# 
# $$I_{n+1}=e-(n+1)I_n$$
# 
# Które wyniki nie są poprawne i dlaczego?
# 
# #### Rozwiązanie:

import math

i = 1 

for n in range (2,21):
    i = math.e - ((n)*i)

    print(n, ":", i)

# %%



