x = [1,2,3,4,5,6,7,8,9,10]
y = []
z= []

#usando list comprehension
# y = [valor_a_adicionar laço condição]

y = [i**2 for i in x]

z = [i for i in x if i%2==1]

print(x)
print(y)
print(z)

"""
for i in x:
	y.append(i**2)

print(x)
print(y)
"""