#map

def dobro(x):
	return x*2

valor = [1,2,3,4,5,6]

valor_dobrado = map(dobro, valor)

valor_dobrado = list(valor_dobrado) #list converte em lista o valor dobrado em lista
print(valor_dobrado)

"""
for i in valor_dobrado: 
	print(i)
"""
#print(dobro(valor)) #imprime a lista duas vezes, nao da o dobro dos numeros
#print(dobro(3))