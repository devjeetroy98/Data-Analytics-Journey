import pandas as pd

sports = {
    'Archery': 'Bhutan',
    'Golf': 'Scotland',
    'Cricket': 'England',
    'Soccer': 'USA',
    'Hockey': 'India'
}

s = pd.Series(sports)
# * iloc means index-location, returns value only
print(s.iloc[3])

# * loc finds by key value pair, retuns value only.
print(s.loc['Golf'])
