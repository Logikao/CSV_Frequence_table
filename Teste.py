"""
import csv
import matplotlib.pyplot as plt

def ler_arquivo_csv(arquivo_csv):
    dados = []
    with open(arquivo_csv, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            dados.append(linha)
    return dados

def tabela_distribuicao_frequencia(dados, coluna):
    frequencias = {}
    for linha in dados[1:]:  # Ignora o cabeçalho
        valor = linha[coluna]
        if valor in frequencias:
            frequencias[valor] += 1
        else:
            frequencias[valor] = 1
    return frequencias

def plotar_tabela_distribuicao(frequencias):
    print("Tabela de Distribuição de Frequência:")
    print("Valor   |   Frequência")
    print("-----------------------")
    for valor, frequencia in frequencias.items():
        print(f"{valor:<8} |   {frequencia}")
        
def plotar_grafico_barras(frequencias):
    valores = list(frequencias.keys())
    frequencias_valores = list(frequencias.values())
    
    plt.bar(valores, frequencias_valores)
    plt.xlabel('Valores')
    plt.ylabel('Frequência')
    plt.title('Gráfico de Barras - Distribuição de Frequência')
    plt.show()

# Ler o arquivo CSV
arquivo_csv = 'McDonalds.csv'  # Coloque o nome do seu arquivo aqui
dados = ler_arquivo_csv(arquivo_csv)

# Mostrar as colunas disponíveis para o usuário escolher
print("Colunas disponíveis:")
for i, coluna in enumerate(dados[0]):
    print(f"{i}: {coluna}")

# Solicitar ao usuário que escolha a coluna
coluna_escolhida = int(input("Escolha o número da coluna que deseja analisar: "))

# Calcular a tabela de distribuição de frequência
frequencias = tabela_distribuicao_frequencia(dados, coluna_escolhida)

# Plotar a tabela de distribuição de frequência
plotar_tabela_distribuicao(frequencias)

# Plotar o gráfico de barras
plotar_grafico_barras(frequencias)

"""

# import packages 
import pandas as pd 
import numpy as np 

# reading csv file as pandas dataframe 
data = pd.read_csv('McDonalds.csv') 
data.head()

