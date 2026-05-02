# Importação das Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Informação do arquivo
df = pd.read_csv("C:/PYTHON/Projeto_Titanic/titanic_dataset.csv")

print(df.head(10))  # Primeiras linhas
print(f"",(df.size), (df.shape), (df.dtypes))   # Tamanho do arquico / Estrutura - Linha vs Coluna e tipo
print(f"",(df.describe()), df.info())   # Descrição do arquivo e Informações e peso em MB

# Identificar as linhas duplicadas para eliminar
duplicateRows = df[df.duplicated()]
print(len(duplicateRows))     # Capiturando o total de itens duplicados

# Verificação de valores nulos
print(df.isnull().sum())

# Renomear Colunas
df = df.rename(columns={'Sex': 'Genero'})
print(df.head(10))

# Ordenar conteúdo por coluna
sorted_df = df.sort_values(by='Age', ascending=True)  # True - do menor para o maior / False - inverso
print(sorted_df)

# Para substituir os dados nan (nulo) por 0
df.replace(np.nan, "0", inplace=True)
print(df)

# Passageiros por Genero(Sexo)
print(df.groupby("Genero")["Survived"].mean())

# Passageiros por classe
print(df.groupby("Pclass")["Survived"].mean())

# Passageiros por Idade
print(df.groupby("Age")["Survived"].mean())

# Passageiros por Cabine
print(df.groupby("Cabin")["Survived"].mean())

# Quantos Sobreviveram
survived_counts = df['Survived'].value_counts(normalize=True)
print(survived_counts)

# Grafico de sobreviventes por Sexo
plt.figure(figsize=(10, 6))
plt.bar(survived_counts.index, survived_counts, color='blue')
plt.title('Proporção de Sobreviventes')
plt.xticks([0, 1], ["Homens: 0 Sobrevivente", 'Mulheres: 1 Sobrevivente'])
plt.show()
