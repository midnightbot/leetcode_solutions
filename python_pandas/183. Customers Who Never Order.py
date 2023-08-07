import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    seen = set()

    ans_rows = []
    ans_cols = ['Customers']
    for indx, r in orders.iterrows():
        seen.add(r['customerId'])


    for indx, r in customers.iterrows():
        if r['id'] not in seen:
            ans_rows.append(r['name'])


    return pd.DataFrame(data=ans_rows, columns = ans_cols)
