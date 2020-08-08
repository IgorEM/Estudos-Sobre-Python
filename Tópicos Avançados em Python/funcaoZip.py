#zip
lista1= [1,2,3,4,5,6,7]
lista2= ["feijao","arroz","prato","pastel","bolacha","tomate", "biscoito"]
lista3= ["R$ 2,00", "R$ 3,49","R$ 2,39", "R$ 6,78","R$ 8,30", "R$ 9,70","R$ 7,50"]

#concatenando 3 listas
for numero, nome, valor in zip(lista1, lista2, lista3):
	print(numero, nome, valor)