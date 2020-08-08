arqtexto = open("arquivo.txt", "r")

texto_completo = arqtexto.read()
#linha = arqtexto.readline()
#linhas = arqtexto.readlines()

print(texto_completo)
#print("----------")
#print(linha)
#print("----------")
#print(linhas) #imprime uma lista

#for i in linhas:
#	print (i)

#read() - Le aruquivo inteiro
#readline() - Le uma linha
#readlines() - Le arquivo e o armazena em uma lista, cada linha eh um elemento

"""Modos de abertura:
r
Descrição	Abre o arquivo para leitura ou o cria, caso não exista. O cursor é posicionado no inicio do arquivo.
r+
Descrição	Abre o arquivo para leitura e escrita ou o cria, caso não exista. O cursor é posicionado no inicio do arquivo.
w
Descrição	Se o arquivo existir, ele é aberto para escrita e o seu tamanho é reduzido para zero (conteúdo do arquivo é apagado). SE não existir, ele é criado na hora.
O cursor é posicionado no inicio do arquivo.
w+
Descrição	Se o arquivo já existir, ele tem tamanho reduzido para zero (conteúdo do arquivo é apagado) e é aberto para escrita e leitura. Se não existir, um novo arquivo é criado.
O cursor é posicionado no inicio do arquivo.
a
Descrição	Abre o arquivo para escrita. Caso não exista, ele é criado e o cursor é posicionado no final do arquivo, As linhas que forem escritas estarão sempre no final do arquivo, mesmo se funções como fseek(6) ou similares forem utilizadas.
a+
Descrição	Abre o arquivo para leitura e escrita. Caso não exista, ele é criado e o cursor é posicionado no final do arquivo, As linhas que forem escritas estarão sempre no final do arquivo, mesmo se funções como fseek(6) ou similares forem utilizadas.
"""