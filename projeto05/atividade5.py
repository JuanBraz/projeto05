'''Fazer uma lista contendo os dias da semana, receba um nome 
do usuário e verifique se ele está na lista.
'''
lista = ['segunda','terça','quarta','quinta','sexta','sábado','domingo']

nome = input('Digite um dia da semana: ')

if nome in lista:
    print(f'{nome} está na lista dos dias da semana')
else:
    print(f'{nome} não está na lista dos dias da semana')