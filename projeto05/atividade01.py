# Criar uma lista pré-definida e adicionar e remover valores solicitados.
lista = [5,8,2,9,1]
print(lista)

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

num1 = 7
lista.append(num1)
print(lista)

num2 = 3
lista.insert(3, num2)
print(lista)

lista[1] = 10
print(lista)

lista.remove(9)
print(lista)
