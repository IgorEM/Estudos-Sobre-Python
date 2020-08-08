# -*- coding: utf-8 -*-
a = 5
b = 3
x = 10
y = 80
if a > b:	
	print("a é maior que b" )

if b > a:
	print("b é maior que a") #b nao é maior que a,nao imprime

if x > y:
	print("x é maior que y")
else:
	print("a variavel x é menor que a variavel y")

#cuidado com a identação, ela define o bloco de codigo
f = 1
g = 1
h = 2

if f == h:
	print("numeros iguais")
elif f < h:
	print("f menor que h") #ímprime só a primeira linha verdadeira
elif h > g:	
	print("h maior que g") #executa a primeira execuçao verdadeira

