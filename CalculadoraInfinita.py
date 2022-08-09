def calculadora(num1, num2, operacao):
    global resultado
    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4:
        resultado = num1 / num2
    elif operacao == 0:
        operacao = 0

    return resultado


operacao = None
print('Calculadora\n')
while (operacao != 0):

    operacao = int(input('Informe a operação:\n1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n0: Sair\n'))

    if operacao == 0:
        print("Encerrando calculadora...")
        break
    elif operacao >= 5:
        print('\n\nEssa opção não existe!!\n--------------------------------\n')
    else:
        num1 = float(input('Informe o primeiro número: '))
        num2 = float(input('\nInforme o segundo número: '))
        resultado = calculadora(num1, num2, operacao)
        print('O resultado é : ' + str(resultado) + ' !')
        print('--------------------fim-----------------------')
