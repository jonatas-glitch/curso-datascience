# Importação das Bibliotecas
import pandas as pd
import seaborn as sms
import matplotlib.pyplot as plt
import numpy as np

# Informação do arquivo
df = pd.read_csv("C:/PYTHON/Projeto_Titanic/titanic_dataset.csv")

# Identificar as linhas duplicadas para eliminar
duplicateRows = df[df.duplicated()]
print(len(duplicateRows))     # Capiturando o total de itens duplicados

# Verificação de valores nulos
print(df.isnull().sum())

# Renomear Colunas
df = df.rename(columns={'Sex': 'Genero'})
print(df.head(10))

# Ordenar conteúdo por coluna
sorted_df = df.sort_values(by='Genero', ascending=True)  # True - do menor para o maior / False - inverso
print(sorted_df)

# Para substituir os dados nan (nulo) por 0
df.replace(np.nan, "0", inplace=True)
print(df)