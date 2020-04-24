import numpy as np
import pandas as pd

df = pd.read_csv(
    '../train.csv', usecols=['Name', 'Pclass', 'Sex', 'Survived', 'Age'])

# * Printing no of empty cells under Age column.
print('No of missing values in Age column is :', df['Age'].isnull().sum())

print(df['Age'].head(20))

# * Filling NaN values with -1.(Does it in entire df)
# df = df.fillna(-1)
# print(df.head(20))

# * Only in column Age
values = {'Age': - 1}
df = df.fillna(value=values)
print(df.head(10))
