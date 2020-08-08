meu_dicionario = {"Ameixa": "É uma fruta vermelha", "Bola": "Objeto redondo que se chuta", "Cachorro":"Pode ser o caramelo"}
#dicionario = {"chave": "valor"}
print(meu_dicionario)
print("\n")
print(meu_dicionario["Ameixa"])
print(meu_dicionario["Cachorro"])
print("\n")

for chave in meu_dicionario:
	print (chave)

print("\n")

for chave in meu_dicionario:
	print (chave + "- " + meu_dicionario[chave])

print("\n")

for i in meu_dicionario.items(): #items retorna tuplas
	print (i)

print("\n")

for i in meu_dicionario.values(): #items retorna tuplas
	print (i)