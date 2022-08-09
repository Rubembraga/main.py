# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import cmath
from typing import List

lista1: List[float] = [1, 2, 3]
lista2: List[float] = [4, 5, 6]
x = complex(lista1[0], lista2[0])
y = complex(lista1[1], lista2[1])
z = complex(lista1[2], lista2[2])
print("O primeiro numero complexo é", end="")
print(x)
print("O segundo numero complexo é", end="")
print(y)
print("O terceiro numero complexo é", end="")
print(z)
print("A soma dos numeros complexos é", end="")
print(x+y+z)
print("A subtração dos numeros complexos é", end="")
print(x-y-z)
print("A multiplicação dos numeros complexos é", end="")
print(x*y*z)
print("A divisão dos numeros complexos é", end="")
print(x/y/z)
print("O primeiro numero real é: ", end="")
print(x.real)
print("O primeiro numero imaginario é: ", end="")
print(x.imag)
print("O segundo numero real é: ", end="")
print(y.real)
print("O segundo numero imaginario é: ", end="")
print(y.imag)
print("O terceiro numero real é: ", end="")
print(z.real)
print("O terceiro numero imaginario é: ", end="")
print(z.imag)
