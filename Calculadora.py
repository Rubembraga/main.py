def calc(v1, v2, op):
    if op == 1:
        return v1 + v2
    elif op == 2:
        return v1 - v2
    elif op == 3:
        return v1 * v2
    elif op == 4:
        return v1 / v2
    else:
        print("Operação Invalida")


v1 = float(input("Insira o primeiro valor:"))
v2 = float(input("Insira o segundo valor:"))
op = int(input("Escolha o valor da operaçao: 1=SOMA, 2= SUBTRAÇÃO, 3= MULTIPLICAÇÃO, 4 DIVISÃO "))

print("Resultado:", calc(v1, v2, op))
