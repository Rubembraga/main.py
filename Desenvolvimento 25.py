def MudaNome():
    novonome = nome.split()
    nome1 = novonome[1].lower()
    nome2 = novonome[0][0:2].lower()
    if len(nome1) > 0 and len(nome2) > 0:
        return nome1+nome2
    else:
        return None


def EscolheSetor():
    try:
        if escolha == 1:
            novoemail = MudaNome()+'.rh@empresa.com'
            return novoemail
        elif escolha == 2:
            novoemail = MudaNome()+'.juridico@empresa.com'
            return novoemail
        elif escolha == 3:
            novoemail = MudaNome()+'.ti@empresa.com'
            return novoemail
    except:
        print('Setor inválido, favor selecione um setor da lista ')

def EscolheEmpresa():
    novaempresa = EscolheSetor().replace('empresa', empresa)
    return print(novaempresa)


cont = False
novoemail = None
while cont == False:
   try:
    print('===== Cadastro de E-mail =====')
    nome = str(input('Digite seu primeiro e último nome: '))
    empresa = str(input('Digite o nome da empresa: '))
    escolha = int(input('''
    Setores:
    [1] RH
    [2] Jurídico
    [3] TI
       
    Selecione o setor onde vai trabalhar:  
    '''))
    print('')
    print('E-mail registrado: ')
    EscolheSetor()
    EscolheEmpresa()
    print('')


    cont = str(input('Deseja continuar? [s / n]\n')).lower().strip()
    try:
        if cont in 's':
           cont = False
        else:
           cont = True
    except:
        print('Dados inválidos')

   except:
       print('Reveja os dados escolhidos')
