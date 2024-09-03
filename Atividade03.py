# declaração das notas feita pelo aluno:
nota1 = int(input('Insira uma nota: '))
nota2 = int(input('Insira uma nota: '))
nota3 = int(input('Insira uma nota: '))
nota4 = int(input('Insira uma nota: '))
nota5 = int(input('Insira uma nota: '))
# declaração da lista: 
media = int((nota1 + nota2 + nota3 + nota4 + nota5) / 5)
# declaração do if e else para as notas do aluno, se ele será aprovado, se ficará de recuperação ou reprovado:
if media >= 7:
    print('Aprovado!!!')
elif media >=5:
    print('Recuperação...')
else:
    print('Reprovado.')