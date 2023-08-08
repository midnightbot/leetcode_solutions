import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    cnt = len(pd.unique(store[store['amount'] > 500]['customer_id']))
    ans_cols = ['rich_count']
    return pd.DataFrame(data=[cnt], columns=ans_cols)
