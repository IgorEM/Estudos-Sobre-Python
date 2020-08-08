a = 2
b = 0
#tentar executar uma linha de codigo que acha que pode dar erro e tratar o erro
try:
	print(a/b)
except:
	print("Não é permitida divisão por 0")
#o programa nao para a execuçao e a proxima linha eh executada
print(a/a)