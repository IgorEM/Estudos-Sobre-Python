minha_string = "O rato roeu a roupa do rei de Roma"
minha_lista = minha_string.split() #converte String para lista
print(minha_lista)
minha_lista1 = minha_string.split("r") #sem os r menusculos, case sensitive
print(minha_lista1)

busca= minha_string.find("rei") #rei começa da posiçao 23
print(busca) #caso não existisse retornava -1
print(minha_string[busca:])

replace = minha_string.replace("do rei", "da rainha")
print(replace)