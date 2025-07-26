import json
import csv
from processamento_dados import Dados

path_json = r'C:\Users\Lucas\Desktop\Projetos\pipeline de dados\data_raw\dados_empresaA.json'
path_csv = r'C:\Users\Lucas\Desktop\Projetos\pipeline de dados\data_raw\dados_empresaB.csv'

# Extração 

dados_empresaA = Dados(path_json, 'json')
dados_empresaB = Dados(path_csv, 'csv')

print(f'Dados "brutos" sem a trasformação\nDADOS DA EMPRESA A:\n{dados_empresaA.dados[:5]}\nDADOS DA EMPRESA B:\n{dados_empresaB.dados[:5]}')
print(f'\nOs dados da empresa A tem: {dados_empresaA.tamanho_dados()} linhas\nOs dados da empreasa B tem {dados_empresaB.tamanho_dados()} linhas')

# Transfomação 

key_mapping = {'Nome do Item': 'Nome do Produto',
               'ClassificaÃ§Ã£o do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}

dados_empresaB.renomeando_colunas(key_mapping)
print(f'\nApós a alteração dos nomes das colunas dos dados da empresa B essas são as colunas:\n{dados_empresaB.nome_colunas}')

dados_fusao = Dados.join(dados_empresaB, dados_empresaA)
print(f'\nApós a junção dos dados, essas são as colunas:\n{dados_fusao.nome_colunas}\nE essa é a quantidade de linhas:\n{dados_fusao.qtd_linhas}')

# Salvar os dados

path_dados_combinados = r'C:\Users\Lucas\Desktop\Projetos\pipeline de dados\data_processed\dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(f'\nAssim que efetuado todas as etapas nosso arquivo vai ser salvo nesse caminho:\n{path_dados_combinados}')
