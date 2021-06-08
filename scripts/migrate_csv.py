###
# Migrates a set of users in CSV that are missing values in a set of Colums.
###

import pandas as pd
csv_file="users.csv"
df = pd.read_csv(csv_file)

# removes all records that NaNs for column1 and column2
df=df.dropna(subset=['column1', 'column2'], how='all')

for index in df.index:
    if 'old_domain.com' in df.loc[index,'mail']:
        email=df.loc[index,'mail'].split('@')
        df.loc[index,'mail'] = email[0]+'@new_domain.com'

df.to_csv(r'./new_users.csv', index = False)
