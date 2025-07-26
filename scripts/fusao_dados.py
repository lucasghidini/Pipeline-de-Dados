import json
import csv
from processamento_dados import Dados


# função de ler e ver o tipo do dado(csv ou json)
def leitura_dos_dados(path, tipo_arquivo):
    dados = []

    if tipo_arquivo == 'csv':
        dados = leitura_csv(path)

    elif tipo_arquivo == 'json':
        dados = leitura_json(path)

    return dados

# função de leitura dos dados .json
def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)

    return dados_json

# função de leitura dos dados .csv
def leitura_csv(path_csv):

    dados_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)

    return dados_csv

# função para ver os nomes dads colunas
def get_columns(dados):
    return list(dados[0].keys())

# função para renomear as colunas dos dados csv
def renomeando_colunas(dados, key_mapping):
    new_dados_csv = []

    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados_csv.append(dict_temp)

    return new_dados_csv

# função para a contagem dos dados
def tamanho_dados(dados):
    return len(dados)

# função de juntar os dados
def join(dadosA, dadosB):
    lista_combinada = []
    lista_combinada.extend(dadosA)
    lista_combinada.extend(dadosB)
    return lista_combinada

# transformação dos dados em tabela
def trasformando_dados_tabela(dados, nome_colunas):
    dados_combinados_tabela = [nome_colunas]

    for row in dados:
        linha = []
        for coluna in nome_colunas:
            linha.append(row.get(coluna, 'Indisponivel'))
        dados_combinados_tabela.append(linha)

    return dados_combinados_tabela

# salvar os dados
def salvando_dados(caminho, dados):
    with open(caminho, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados)


path_json = r'C:\Users\Lucas\Desktop\Projetos\pipeline de dados\data_raw\dados_empresaA.json'
path_csv = r'C:\Users\Lucas\Desktop\Projetos\pipeline de dados\data_raw\dados_empresaB.csv'


dados_empresaA = Dados(path_json, 'json')




# # leitura
# dados_json = leitura_dos_dados(path_json, 'json')
# nome_colunas_json = get_columns(dados_json)
# print(f'nome das colunas do arquivo json: {nome_colunas_json}')

# dados_csv = leitura_dos_dados(path_csv, 'csv')
# nome_colunas_csv = get_columns(dados_csv)
# print(f'Nome das colunas do arquivo csv: {nome_colunas_csv}')

# # transformação dos dados
# key_mapping = {'Nome do Item': 'Nome do Produto',
#                'ClassificaÃ§Ã£o do Produto': 'Categoria do Produto',
#                'Valor em Reais (R$)': 'Preço do Produto (R$)',
#                'Quantidade em Estoque': 'Quantidade em Estoque',
#                'Nome da Loja': 'Filial',
#                'Data da Venda': 'Data da Venda'}

# dados_csv = renomeando_colunas(dados_csv, key_mapping)
# nome_colunas_csv = get_columns(dados_csv)
# print(f"Novas colunas do arquivo csv: {nome_colunas_csv}")

# # Calculando o tamanho dos dados
# tamanho_dados_csv = tamanho_dados(dados_csv)
# print(f'Tamanho dos dados csv: {tamanho_dados_csv}')

# tamanho_dados_json = tamanho_dados(dados_json)
# print(f'Tamanho dos dados json: {tamanho_dados_json}')

# # Junção dos dados
# dados_fusao = join(dados_csv, dados_json)
# nomes_colunas_fusao = get_columns(dados_fusao)
# tamanho_dados_fusao = tamanho_dados(dados_fusao)

# print(nomes_colunas_fusao)
# print(tamanho_dados_fusao)

# # salvando dados

# # salvando os dados em uma nova estrutura, não mais em uma lista
# dados_fusao_tabela = trasformando_dados_tabela(
#     dados_fusao, nomes_colunas_fusao)

# path_dados_combinados = r'C:\Users\Lucas\Desktop\Projetos\pipeline de dados\data_processed\dados_combinados.csv'

# salvando_dados(path_dados_combinados, dados_fusao_tabela)
# print(path_dados_combinados)
