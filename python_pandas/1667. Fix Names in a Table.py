import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:

    for indx, r in users.iterrows():
        users.loc[indx, 'name'] = (r['name'][0].upper())+(r['name'].lower())[1:]

    users = users.sort_values(by='user_id')
    return users
