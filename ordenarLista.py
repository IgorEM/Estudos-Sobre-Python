lista =[4564,87,41,654,54,651,1,456,3,9,967,6,548,4]
cores = ["azul", 4,"vermelho", 5, "amarelo", "verde", True, "branco"]
reais = [1.487, 4.8, 1.12, 2.7, 1.21]

lista.sort() #altera a lista existente e ordena
print(lista)

listaNovaOrdenada = sorted(reais) # cria nova lista sorted
print(listaNovaOrdenada)

reais.sort(reverse=True) #reverse=True - ordena decrescente
print(reais)

cores.reverse() #reverte a lista
print(cores)


