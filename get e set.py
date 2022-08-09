from time import sleep

class resultado:
    def __init__(self, fabrica, producao):
        self.fabrica = fabrica
        self.producao = producao

    def get_fabrica(self):
        return self.fabrica

    def get_producao(self):
        return self.producao

    def set_resultado_fabrica(self, ResFabrica):
        self.fabrica = ResFabrica

    def set_resultado_producao(self, ResProducao):
        self.producao = ResProducao

#OBJETOS CRIADOS

abreulima = resultado('Abreu e Lima', 250)
goiana = resultado('Goiana', 148)


# HOSTÓRICO DO CASE

print('======== RESULTADO 2020 ========')
sleep(1)
print(' Unidade Fabril: ', abreulima.get_fabrica(), '\n', 'Produção: ', abreulima.get_producao(), 'ton\n')
sleep(2)
print(' Unidade Fabril: ', goiana.get_fabrica(), '\n', 'Produção: ', goiana.get_producao(), 'ton\n')
sleep(2)

#REGRAS DE NEGÓCIO

print('Unidades produtivas que incrementarem em 15% a sua produção. Terão acesso a PL\n')
sleep(2)

print('======== METAS PARA 2021 ========')
sleep(1)
print(' Unidade Fabril: ', abreulima.get_fabrica(), '\n', 'Produção: ', abreulima.get_producao(), '>>>>>', abreulima.get_producao() + (abreulima.get_producao() * (15/100)), 'ton\n')
sleep(2)
print(' Unidade Fabril: ', goiana.get_fabrica(), '\n', 'Produção: ', goiana.get_producao(), '>>>>>', goiana.get_producao() + (goiana.get_producao() * (15/100)), 'ton\n\n')
sleep(3)

abreumeta2021 = abreulima.get_producao() + abreulima.get_producao() * 15/100
goianameta2021 = goiana.get_producao() + goiana.get_producao() * 15/100


#ENTRADA DE DADOS E VALIDAÇÃO

print('======== RESULTADO 2020 ========')
sleep(1)
print(' Unidade Fabril: ', abreulima.get_fabrica())
cont = False
while cont == False:
    try:
        novatonabreu = int(input(' \033[4;31m Digite a Produção(ton) realizada em 2021:\033[m '))
        cont = True
    except:
        print('Reveja os dados e tente novamente')

abreulima.set_resultado_producao(novatonabreu)
print(' Produção: ', abreulima.get_producao(), 'ton\n')

print('\n')

print(' Unidade Fabril: ', goiana.get_fabrica())

cont = False
while cont == False:
    try:
        novatongoiana = int(input(' \033[4;31m Digite a Produção(ton) realizada em 2021:\033[m '))
        cont = True
    except:
        print('Reveja os dados e tente novamente')

goiana.set_resultado_producao(novatongoiana)
print(' Produção: ', goiana.get_producao(), 'ton\n')

print('Processando...')
sleep(3)


#RESULTADOS DO CASE

if novatonabreu >= abreumeta2021:
    print(' \033[1;32m PL liberado \033[m para', abreulima.get_fabrica())
else:
    print(' \033[1;33m PL bloqueada \033[m para', abreulima.get_fabrica(), ' Tentaremos ano que vem!')
if novatongoiana >= goianameta2021:
    print(' \033[1;32m PL liberado \033[m para', goiana.get_fabrica())
else:
    print(' \033[1;33m PL bloqueada \033[m para', goiana.get_fabrica(), ' Tentaremos ano que vem!')


