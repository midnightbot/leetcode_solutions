import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:

    ans = employee.groupby('managerId')['id'].agg(['count']).reset_index()
    ans = ans.loc[ans['count']>=5, ['managerId']]
    ans = employee.loc[employee['id'].isin(ans['managerId']),['name']]

    return ans
