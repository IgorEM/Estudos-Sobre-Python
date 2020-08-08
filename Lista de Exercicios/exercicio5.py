#5. Escreva um programa que receba dois números e um sinal,
#faça a operação matemática definida pelo sinal. 

n1 = int(input("Digite o primeiro numero: "))
sinal = input("Digite um sinal de operação (+ , -, * ou / ): ")
n2 = int(input("Digite o segundo numero: "))

if sinal == "+":
	op = n1 + n2

elif sinal == "-":
	op = n1 - n2

elif sinal == "*":
	op = n1 * n2

elif sinal == "/":
	op = n1 / n2

else:
	print("Sinal inválido.")

print("Resultado: ", op)