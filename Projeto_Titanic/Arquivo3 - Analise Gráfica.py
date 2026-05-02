# Importação das Bibliotecas
import pandas as pd
import seaborn as sms
import matplotlib.pyplot as plt

# Informação do arquivo
df = pd.read_csv("C:/PYTHON/Projeto_Titanic/titanic_dataset.csv")

# Quantos por cento Sobreviveram
survived_counts = df['Survived'].value_counts(normalize=True)

# Grafico de sobreviventes por idade
plt.figure(figsize=(10, 6))
plt.bar(survived_counts.index, survived_counts, color='blue')
plt.title('Proporção de Sobreviventes')
plt.xticks([0, 1], ["Homens: 0 Sobrevivente", 'Mulheres: 1 Sobrevivente'])
plt.show()
