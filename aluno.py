boletim = list()
nome = str(input('nome: '))
faltas = int(input('Faltas: '))
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = float(nota1 + nota2)/2
status = str()
if media < 7 or faltas > 3:
    status = 'Reprovado'
else:
    status = 'Aprovado'
boletim.append([nome, [nota1, nota2], faltas, media, status])
print(boletim)
