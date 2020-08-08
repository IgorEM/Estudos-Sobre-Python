#3. Escreva um programa que resolva uma equação de segundo grau.   
from math import sqrt
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
print("\n")
bquadrado = b**2
print("b ao quadrado= ", bquadrado, "\n")

mult = -4*a*c
print("-4*a*c= ", mult, "\n")

delta = bquadrado + mult
print("delta= ", delta, "\n")

raiz_delta = sqrt(delta)
print("raiz quadrada de delta= ", raiz_delta, "\n")
 
if raiz_delta < 0:
    print("Delta negativo", "\n")
else:
    x1 = (-b + raiz_delta)/(2*a)
    x2 = (-b - raiz_delta)/(2*a)

print(" x1 = (-b + raiz_delta)/(2*a) \n x1= ", x1, "\n")
print(" x2 = (-b - raiz_delta)/(2*a) \n x2= ", x2, "\n")