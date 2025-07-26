import json
import csv


# Criação de classe Dados
class Dados:

    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dos_dados()
        self.nome_colunas = self.get_columns()
        self.qtd_linhas = self.tamanho_dados()
        

        
    def leitura_dos_dados(self):
        dados = []

        if self.tipo_dados == 'csv':
            dados = self.leitura_csv()

        elif self.tipo_dados == 'json':
            dados = self.leitura_json()
        
        elif self.tipo_dados == 'list':
            dados = self.path
            self.path = 'lista em memoria'

        return dados

    
    def leitura_json(self):
        dados_json = []
        with open(self.path, 'r') as file:
            dados_json = json.load(file)

        return dados_json

    
    def leitura_csv(self):

        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)

        return dados_csv
    
    def get_columns(self):
        
        return list(self.dados[0].keys())
    
    def renomeando_colunas(self, key_mapping):
        new_dados = []

        for old_dict in self.dados:
            dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados.append(dict_temp)

        self.dados = new_dados
        self.nome_colunas = self.get_columns()

    def tamanho_dados(self):
        return len(self.dados)
    
    def join(dadosA, dadosB):
        lista_combinada = []
        lista_combinada.extend(dadosA.dados)
        lista_combinada.extend(dadosB.dados)

        return Dados(lista_combinada, 'list')
    
    def trasformando_dados_tabela(self):
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'Indisponivel'))
            dados_combinados_tabela.append(linha)

        return dados_combinados_tabela
        
    def salvando_dados(self, path):
        
        dados_combinados_tabela = self.trasformando_dados_tabela()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)