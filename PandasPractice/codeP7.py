import numpy as np
import pandas as pd

df = pd.read_csv(
    '../train.csv', usecols=['Name', 'Pclass', 'Sex', 'Survived', 'Age'])

# * Print total count
print('Total no of Passangers =', len(df))

# * Print count of those who survived
print('Total no of Passangers survived =', len(df[df['Survived'] == 1]))

# * Print count of those who survived and are female
print('Total no of Passangers survived and are female=', len(
    df[(df['Survived'] == 1) & (df['Sex'] == 'female')]))

# * Print how many passangers travelling via Pclass: 1 are alive!
print('Total no of Passangers survived and were trvelling in Pclass 1 is=', len(
    df[(df['Survived'] == 1) & (df['Pclass'] == 1)]))

# * Print how many passangers were tavelling Pclass 1 and were female.
print('Total no of Passangers who were female and were trvelling in Pclass 1 is=', len(
    df[(df['Sex'] == 'female') & (df['Pclass'] == 1)]))
