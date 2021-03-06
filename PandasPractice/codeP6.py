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

# * Indexing
# * Providing 20 % discount
costs = df['Cost']
costs *= 0.8
print(df)
