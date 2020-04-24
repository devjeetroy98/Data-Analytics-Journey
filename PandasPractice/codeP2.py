import pandas as pd

sports = {
    'Archery': 'Bhutan',
    'Golf': 'Scotland',
    'Cricket': 'England',
    'Soccer': 'USA',
    'Hockey': 'India'
}
s = pd.Series(sports)
print(s)
