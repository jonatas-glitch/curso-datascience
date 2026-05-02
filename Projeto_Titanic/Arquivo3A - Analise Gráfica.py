# Importação das Bibliotecas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Informação do arquivo
df = pd.read_csv("C:/PYTHON/Projeto_Titanic/titanic_dataset.csv")

# Total de Passageiros por faixa etária de idade
sns.boxplot(y=df['Age'], color="pink")
plt.title('Distribuição dos Passageiros por Idade')
plt.show()