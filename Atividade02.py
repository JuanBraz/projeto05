lista = ['janeiro', 'fevereiro', 'maio', 'março', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
print(f'Verificação de índice número 4 (mês junho) {lista[5]}')

# if para determinar se o mês de junho está na lista
if "junho" in lista:
    print('O mês de junho está na lista')
else:
    print('O mês de junho não está na lista')

lista.insert(3, 'Abril') # inserir um valor/nome à lista
print(lista)

lista[6] = 'Dezembro' # substitui o índice escolhido

lista.pop(10) # Elimina o índice