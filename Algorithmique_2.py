from math import *

n = int(input("entrer un nombre >= 1: "))
somme = 0
if (n>=1):
    for i in range (1, n+1):
        somme += i

print ("La somme des entiers de 1 à", n, "est:", somme)