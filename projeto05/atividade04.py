num1 = input('Insira um numero: ')
num2 = input('Insira o segundo numero: ')
#Requisito dois numeros ao usuario

if num1 > num2:
    print(f'O primeiro numero é maior ')
#caso o primeiro numero for maior faço a impressão indicando isso
elif num1 < num2:
    print(f'O segundo numero é maior ') 
#caso o segundo numero for maior faço a impressão indicando isso
else:
    print(f'Os numeros são iguais')
#caso os dois numeros estejam iguais imprimo na tela indicando isso