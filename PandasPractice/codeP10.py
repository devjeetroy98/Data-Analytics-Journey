import numpy as np
import pandas as pd

df = pd.read_csv(
    '../train.csv', usecols=['Name', 'Pclass', 'Sex', 'Survived', 'Age'])

print(df.head(5))

df2 = df.groupby('Pclass')
# * Fetches only 1st row from each group
print(df2.first())

# * Finding how many people travelled in each class.
print(df2.get_group(1)['Name'].count())
print(df2.get_group(2)['Name'].count())
print(df2.get_group(3)['Name'].count())
print(df['Name'].count())
