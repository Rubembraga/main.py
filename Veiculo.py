rodas = int(input('Quantidade de rodas do veiculo:'))
peso = int(input('Qual o peso do veiculo:'))
cap = int(input('Qual a capacidade de passageiros do veiculo:'))
hab = str()
if rodas < 4:
    hab = "A"
elif (rodas >= 4) and (peso > 6000):
    hab = "E"
elif (rodas == 4) and (peso <= 3500) and (cap <= 8):
    hab = "B"
elif (rodas >= 4) and (peso > 3500) and (peso < 6000):
    hab = "C"
else:
    hab = "D"
print('A carteira de habilitação necessaria para esse tipo de veiculo é:', hab)
