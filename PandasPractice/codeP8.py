import numpy as np
import pandas as pd

df = pd.read_csv(
    '../train.csv', usecols=['Name', 'Pclass', 'Sex', 'Survived', 'Age'])

# * Setting name as the index of the DataFrame
df = df.set_index('Name')
print(df.head(5))

# * Dropping Age from the database
df = df.drop(columns=['Age'], axis=1)
print(df.head(5))

# * Resettingindex to serial no
df = df.reset_index()
print(df.head(5))

# * Getting unique value presentin Pclass column
# * Returns a list of unique values.
s = df['Pclass'].unique()
print(s)
