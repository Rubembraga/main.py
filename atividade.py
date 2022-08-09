#Importando o pandas e criando a função de cabeçalho
import pandas as pd
def cabecalho(msg):
    print('=-'*21)
    print(msg.center(41))
    print('=-'*21)
    print('')


#Importando o DataFrame
df = pd.read_csv('notas_alunos.csv', sep=';', decimal=',')

#chamando a função do cabeçalho
cabecalho('Desenvolvimento 20 - Trabalhando com .CSV')

#Transformando o tipo de dados
df['nota_1'] = df['nota_1'].astype(float)
df['nota_2'] = df['nota_2'].astype(float)
df['faltas'] = df['faltas'].astype(float)

#Calculando a média dos alunos
media = (df['nota_1'] + df['nota_2']) / 2
df['media'] = media

#mostrando o DataFrame
print(df)

#Usando o .loc para criar a coluna de situação com base na média e faltas dos alunos
df.loc[(df['media'] >= 7) & (df['faltas'] < 5), 'Situação'] = 'Aprovado'
df.loc[(df['media'] < 7) | (df['faltas'] >= 5), 'Situação'] = 'Reprovado'

#Criando as variáveis de maior número de faltas, médias e média geral
faltamax = df['faltas'].max()
mediamax = df['media'].max()
mediag = df['media'].sum() / df['media'].count()

#Mostrando os dados finais
print(f'\nMaior número de faltas foram',(faltamax),'faltas')
print(f'Aluno de maior média fez,',(mediamax),'pontos')
print(f'Média geral da turma foi,',(mediag),'pontos')



