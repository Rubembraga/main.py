def calculadora_idade(nome, ano_nasc):
    ano_atual = 2022
    idade = ano_atual - ano_nasc
    idade = '{} em 2022 você fez ou fará {} anos.'.format(nome, idade)
    return idade


nome = str(input('Informe seu nome completo: '))
erro = True
while erro:
    try:
        ano_nasc = int(input('Informe o seu ano de nascimento: '))
        if 1922 <= ano_nasc <= 2021:
            print(calculadora_idade(nome, ano_nasc))
            erro = False
        else:
            print('Ano de nascimento informado é invalido!')
            erro = True
    except:
        print('Informação inválida!')
        erro = True
