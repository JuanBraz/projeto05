# declaração dos números pelo usuário:
num1 = input('Insira um número: ')
num2 = input('Insira um número: ')
num3 = input('Insira um número: ')
num4 = input('Insira um número: ')
# declaração da lista:
lista = [num1, num2, num3, num4]
# organização dos valores em ordem decrescente para imprimir o maior e o menor valor:
lista.sort()
# printando o maior e menor valor:
print("O maior valor é: ", lista[3])
print("O menor valor é: ", lista[0])