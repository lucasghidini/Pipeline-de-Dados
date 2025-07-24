import json
import csv

# caminho do arquivo json
path_json = r'C:\Users\Lucas\Desktop\Projetos\pipeline de dados\data_raw\dados_empresaA.json'

# função de leitura dos dados .json
def  leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json



# caminho do arquivo csv
path_csv = r'C:\Users\Lucas\Desktop\Projetos\pipeline de dados\data_raw\dados_empresaB.csv'

# função de leitura dos dados .sv   
def leitura_csv(path_csv):
    dados_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter= ',')
        for row in spamreader:
            dados_csv.append(row)
    return dados_csv




dados_csv = leitura_csv(path_csv)
dados_json = leitura_json(path_json)
print(dados_csv[0])
print(dados_json[0])