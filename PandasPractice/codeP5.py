import pandas as pd

purchase_1 = pd.Series({
    'Name': 'Chris',
    'Item Purchased': 'Dog Food',
    'Cost': 22.50
})
purchase_2 = pd.Series({
    'Name': 'Jun',
    'Item Purchased': 'Cat Food',
    'Cost': 20.50
})
purchase_3 = pd.Series({
    'Name': 'Ravi',
    'Item Purchased': 'Fish Food',
    'Cost': 15.50
})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3],
                  index=['Store 1', 'Store 2', 'Store 3'])

# * Returns first 10 rows!
print(df.head(10))
print('-----------------------------')

# * Finding Transpose of a DataFrame
df = df.T
print(df.head(10))
print('-----------------------------')
df = df.T
print(df.head(10))

# * Getting all the rows with specified columns
print('-----------------------------')
print(df.loc[:, ['Name', 'Cost']])
print('-----------------------------')

# * Dropping a row from the Dataframe
df = df.drop('Store 3')
print(df)
print('-----------------------------')

# * Entering a new row into the Dataframe
df = df.append(pd.Series({
    'Name': 'Ravi',
    'Item Purchased': 'Fish Food',
    'Cost': 15.50
}), 'Store 3')
print(df)
print('-----------------------------')

# * Setting a new column 'Location' to 'USA'
df['Location'] = 'USA'
print(df)
