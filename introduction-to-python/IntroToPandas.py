import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('C:/Users/Vetea/Documents/00_MASTER2/S1/PYTHON/data-science-tutorials/introduction-to-python/train.csv')
print(df.head())

print(df.isnull().sum())

# Who are the survivor of the Titanic

# Survival rate
print(df.groupby('Survived')['PassengerId'].agg(['count']))
counts = df.groupby('Survived')['PassengerId'].agg(['count']).reset_index()
fig = px.bar(counts, x='Survived', y='count', title="Nombre de passagers par survie")
fig.show()

# Survival rate depending on gender
print(df.groupby(['Survived', 'Sex'])['PassengerId'].agg(['count']))

print(df.groupby(['Survived', 'Sex'])['PassengerId'].agg(['count']).unstack())
counts1 = df.groupby(['Survived', 'Sex'])['PassengerId'].count().reset_index()
fig1 = px.bar(counts1, x='Survived', y='PassengerId', color='Sex', barmode='group', title='Passenger by survival and by sex')
fig1.show()
