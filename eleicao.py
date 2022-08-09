from enum import Enum


class Candidatos(Enum):
    candidato_X = 889
    candidato_Y = 847
    candidato_Z = 515
    branco = 0


verdade = True
eleitoVotos = 0
xVotos = 0
yVotos = 0
zVotos = 0
brancosVotos = 0
nulosVotos = 0
while verdade:
    voto = input('Digite o número do candidato (ou "fim" para encerrar): ')
    if voto == 'Fim' or voto == 'fim' or voto == 'FIM':
        if (xVotos > yVotos) and (xVotos > zVotos):
            eleitoNome = "Candidato X"
            eleitoVotos = xVotos
        elif (yVotos > xVotos) and (yVotos > zVotos):
            eleitoNome = "Candidato Y"
            eleitoVotos = yVotos
        elif (zVotos > yVotos) and (zVotos > yVotos):
            eleitoNome = "Candidato Z"
            eleitoVotos = yVotos
        else:
            eleitoVotos = xVotos
            eleitoNome = "EMPATE"

        print('FIM DA VOTAÇÃO')
        print("\n", "O Candidato Vencedor foi: ", eleitoNome, "com o total de ", eleitoVotos, "votos", "\n")
        print(repr(Candidatos.candidato_X))
        print(xVotos)
        print(repr(Candidatos.candidato_Y))
        print(yVotos)
        print(repr(Candidatos.candidato_Z))
        print(zVotos)
        print(repr(Candidatos.branco))
        print(brancosVotos)
        print("Votos Nulos: ")
        print(nulosVotos)
        verdade = False

    if voto == "889":
        xVotos += 1
    elif voto == "847":
        yVotos += 1
    elif voto == "515":
        zVotos += 1
    elif voto == "0":
        brancosVotos += 1
    else:
        nulosVotos += 1
