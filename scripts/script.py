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


path_json = r'C:\Users\Lucas\Desktop\Projetos\pipeline de dados\data_raw\dados_empresaA.json'
path_csv = r'C:\Users\Lucas\Desktop\Projetos\pipeline de dados\data_raw\dados_empresaB.csv'


dados_json = leitura_dos_dados(path_json, 'json')
print(dados_json[0])

dados_csv = leitura_dos_dados(path_csv, 'csv')
print(dados_csv[0])