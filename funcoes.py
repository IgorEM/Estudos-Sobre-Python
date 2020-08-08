def soma(x,y):
	print(x,"+",y,"=", x + y)
def multiplicacao(a,b):
	print(a,"*",b,"=", a*b)

soma(485,989)
multiplicacao(10,4)

def adicao(x,y):
	return x+y

def mult(x,y):
	return x*y

def sub(x,y):
	return x-y

print("\n")

i = adicao(2,2) #4
j = mult(4,10) #40
h = sub(8,4) #4

print( sub( mult(i,h), adicao(j,i) ) ) #16-44 = -28