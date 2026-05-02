# Importação das Bibliotecas
import pandas as pd

# Informação do arquivo
df = pd.read_csv("C:/PYTHON/Projeto_Titanic/titanic_dataset.csv")

print(df.head())  # Primeiras linhas
print(f"",(df.size), (df.shape), (df.dtypes))   # Tamanho do arquico / Estrutura - Linha vs Coluna e tipo
print(f"",(df.describe()), df.info())   # Descrição do arquivo e Informações e peso em MB
