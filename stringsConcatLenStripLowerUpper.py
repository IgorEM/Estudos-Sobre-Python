a = "Igor"
b = "Eduardo"
e = "                 "

concatenar = e + a + " " + b + "\n" 
print(concatenar)

tamanho = len(concatenar)
print(tamanho)

print(a[1],b[2],a[1],b[2]," ",b[1],b[3],b[5],b[3])

print(concatenar[2:8])

c = "MAIUSCÚLO-menuscúlo"
print(c)
print(concatenar.strip()) #tira caracteres especiais do começo e do fim
print(c.lower()) #tudo menusculo
print(c.upper()) #tudo maiusculo