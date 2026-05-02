# Importação das Bibliotecas
import pandas as pd

# Informação do arquivo
df = pd.read_csv("C:/PYTHON/Projeto_Titanic/titanic_dataset.csv")

# Qauntos Sobreviveram
survived_counts = df['Survived'].value_counts(normalize=True)
print(survived_counts)

# Passageiros por Genero(Sexo)
print(df.groupby("Sex")["Survived"].mean())

# Passageiros por classe
print(df.groupby("Pclass")["Survived"].mean())

# Passageiros por Idade
print(df.groupby("Age")["Survived"].mean())

# Passageiros por Cabine
print(df.groupby("Cabin")["Survived"].mean())