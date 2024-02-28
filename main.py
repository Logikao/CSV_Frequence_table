#Grupo: Rafael Vargas Serenato e Lucas Braga Schuck

"""                                                        Dados da atividade 
                                                                 V
Nome da base: McDonalds.csv
Tipo de dano:  Dados financeiros de uma filial do McDonalds
Data de coleta dos dados:  2002 - 2022
Quantas variáveis possui:  4                    Link: https://www.kaggle.com/datasets/mikhail1681/mcdonalds-financial-statements-2002-2022?rvi=1
    Indica-los:
#! Indicar se existem informações já publicadas sobre seu uso e, em caso positivo, onde foi publicado, por quem, o quê
"""

""" ======================================================================
    Indice:
        '#' - indica o comentário do que código faz
        '#!' - indica a parte da atividade que está fazendo
        '#?' - indica campos para testes
====================================================================== """

#Bibliotecas
import csv, math 
from tabulate import tabulate
import matplotlib as plt
import pandas as pd
import numpy as np


#Variáveis

#   '' tabela
table = []
head_table = ["Classes","fi","xi","Fi"]  #?l.sort(key=lambda x: x[2]) //exemplo

#   '' CSV
csv_file_brut = 'McDonald.csv' #Pegando o arquivo
csv_file = []


#Importar a base de dados

with open(csv_file_brut, 'r') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        csv_file.append(line)

data = pd.read_csv('McDonalds.csv') 
data.head()


#Funções
    
#   '' para pegar o MAIOR número
def find_largest(file):
    csv_reader = csv.reader(file)
    first_register = next(csv_reader)  #Obter o primeiro registro

    largest = float(first_register[0])

    for line in csv_reader:
        for number_str in line:
            number = float(number_str)
            if number > largest:        #Procupa pelo MAIOR número
                largest = number

    return largest

#   '' para pegar o MENOR número
def find_smallest(file):
    csv_reader = csv.reader(file)
    first_register = next(csv_reader)   

    smallest = float(first_register[0])

    for line in csv_reader:
        for number_str in line:
            number = float(number_str)
            if number < smallest:       #Procura pelo MENOR número
                smallest = number

    return smallest

#   '' para contar os elementos da base
def count_lines(file):
    count = 0
    for i in file:
        count += 1

    return count

#   '' de números do intervalo
def fi(start,end):
    var = 0

    for i in csv_file:
        if i in range(start,end):
            var += 1
            
    return var

#   '' de ponto médio
def xi(start,end):
    var = (start + end) / 2

    return var

#   '' de acumulo de números do intervalo
def Fi(start,end):
    #Fi = fi novo + fi antigo
    var = 0

    for i in csv_file:
        if i in range(start,end):
            var += 1

    return var

#   '' para plotar o gráfico
def plot_graphic(frequecy):
    value = list(frequecy.keys())
    frequecy_value = list(frequecy.values())
    
    plt.bar(value, frequecy_value)
    plt.xlabel('Valores')
    plt.ylabel('Frequência')
    plt.title('Gráfico de Barras - Distribuição de Frequência')
    plt.show()


#!Amp total -> maior valor - menor valor = A
A = (find_largest(csv_file)) - (find_largest(csv_file))

#!Classes -> i = 1 + 3,3 . log(N)/log(10)  //N sendo o número de elementos (arredondar para cima)
N = count_lines(csv_file)
I = math.ceil(1 + (3,3 * (math.log(N)/math.log(10))))

#!Amp das classes -> H = A/i //arredondar para cima
H = math.ceil(A/I)
    
#!Tabela -> Menor valor da base + H = X
#!                  X + H = Y
#!                  Y + H = Z  //assim por diante, até completar o número de classes
#!
#!      fi -> contar nos números do intervalo entre os números //Contar com os números da base dentro do intervalo de valores
#!      xi -> número médio da classe //número do meio, pode ser quebrado
#!      Fi -> frequencia acumulada //vai somar os fi das classes (Ex: classe 1 = 4, classe 2 = 3 + classe 1 == 7)
#!      
#!      !! O usuário escolhe a variável para plotar o gráfico !!



X = (find_smallest + H)
table.append(X,fi((find_smallest),X),xi(),Fi())
for x in I:
    table.append(x,fi(),xi(),Fi())

#? print(tabulate(table, headers=head_table, tablefmt="grid"))
    
#?  df = data['species'].value_counts() 
#? print(df) 

#Escolha do usuário
print("Colunas disponíveis:")
for i, coluna in enumerate(dados[0]):
    print(f"{i}: {coluna}")




