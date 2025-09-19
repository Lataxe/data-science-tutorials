import pandas as pd

df = pd.read_csv('C:/Users/Vetea/Documents/00_MASTER2/S1/PYTHON/data-science-tutorials/introduction-to-python/train.csv')
print(df.head())

print(df.isnull().sum())

# Who are the survivor of the Titanic

# Survival rate
print(df.groupby('Survived')['PassengerId'].agg(['count']))

