#funcao Reduce
from functools import reduce

def soma(x,y):
	return x+y

lista = [4,9,3,2,5]

somaTodosElementosDaLista = reduce (soma, lista)
print(somaTodosElementosDaLista)