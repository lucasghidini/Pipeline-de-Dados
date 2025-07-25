import json
import csv

# função de ler e ver o tipo do dado(csv ou json)
def leitura_dos_dados(path, tipo_arquivo):
    dados = []
    
    if tipo_arquivo == 'csv':
        dados = leitura_csv(path)

    elif tipo_arquivo == 'json':
        dados = leitura_json(path)

    return dados


# função de leitura dos dados .json
def  leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)

    return dados_json


# função de leitura dos dados .csv   
def leitura_csv(path_csv):

    dados_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter= ',')
        for row in spamreader:
            dados_csv.append(row)

    return dados_csv

# função para ver os nomes dads colunas
def get_columns(dados):
    return list(dados[0].keys())

def renomeando_colunas(dados, key_mapping):
    new_dados_csv = []

    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados_csv.append(dict_temp)
  

    return new_dados_csv

# função de juntar os dados
def juntando_dados(dadosA, dadosB):
    lista_combinada = []
    lista_combinada.extend(dadosA)
    lista_combinada.extend(dadosB)
    return lista_combinada

path_json = r'C:\Users\Lucas\Desktop\Projetos\pipeline de dados\data_raw\dados_empresaA.json'
path_csv = r'C:\Users\Lucas\Desktop\Projetos\pipeline de dados\data_raw\dados_empresaB.csv'

key_mapping = {'Nome do Item': 'Nome do Produto',
                'ClassificaÃ§Ã£o do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

# leitura
dados_json = leitura_dos_dados(path_json, 'json')
nome_colunas_json = get_columns(dados_json)
print(f'nome das colunas do arquivo json: {nome_colunas_json}')

dados_csv = leitura_dos_dados(path_csv, 'csv')
nome_colunas_csv = get_columns(dados_csv)
print(f'Nome das colunas do arquivo csv: {nome_colunas_csv}')

# transformação dos dados
dados_csv = renomeando_colunas(dados_csv, key_mapping)
nome_colunas_csv = get_columns(dados_csv)
print(f"Novas colunas do arquivo csv: {nome_colunas_csv}")

# junçao dos dados






