lista_frutas = ["tomate", "uva", "limao", "abacate"]
lista_inteiros = [4,6,7,5,7,2,9,7,1,3,5,8,4]

print(lista_frutas)
print(lista_inteiros)

tamanho = len(lista_frutas)
tamanho2 = len(lista_inteiros)
print(tamanho)
print(tamanho2)


lista_frutas.append("melancia") #append adiciona o valor ao final da lista
print(lista_frutas)


if 7 in lista_inteiros:
	print("7 está na minha lista_inteiros")


lista_frutas.append("maracuja")


if "maracuja" in lista_frutas:
	print("maracuja ésta na lista_frutas")

del lista_frutas[1:3] #apagou uva e limao
print(lista_frutas)