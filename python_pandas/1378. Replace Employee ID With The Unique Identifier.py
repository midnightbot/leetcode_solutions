import pandas as pd

def replace_employee_id(e: pd.DataFrame, eu: pd.DataFrame) -> pd.DataFrame:

    ans = pd.merge(e, eu, how='left',on='id')
    return ans[['unique_id','name']]
