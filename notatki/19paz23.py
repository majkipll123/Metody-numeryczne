#Żle uwarunkowane macierze powodują brak wraźliwości na małe błedy 
#bardzo małe zmiany w danych wejsciowych powodują duże zmiany w wynikach
#macierz Hilberta 
import numpy as np
from numpy import linalg as LA 
'''
for j in range (2,17):
    print ("%3d  %e"%(j, LA.cond(LA.hilbert(j),np.inf)))

n=4 
while n<17:
    H= LA.hilbert(n)
    b=np.zeros(n)

    for i in range (n):
        b[i]=np.sum(H[i])
    
    x= LA.solve(H,b)
    print('\nn=',n,' x=',x)
    n=n*2

    #żęby sprawdzic czy wynik jest poprawny musimy pomnożyć wynik przez macierz H
'''
"""modyfikacja gausa-seidla mozna to robic ale wymaga to bardzo duzo iteracji 
i jest to bardzo wolne 
jezeli dokonujemy przeliczenia z starej wersji wektora na nowy 
to wtedy wykorzystywane sa stare wersje wektora, w modyfikacji gausa chodzi o to wierzymy w to ze nastepny krok jest lepszym przyblizeniem i podstawiamy nowe wartosci do k-1 
to działa troche szybciej niz maciez jakobiego 
metoda halleya 
skuteczniejsza w przypadkach pierwiastkow wielokrotnych 
wredne pierwiastki wielokrotne sa rozne czasem skomplikowane i klopotliwe niekoniecznie najlepsze
"""

