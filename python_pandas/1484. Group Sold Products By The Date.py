import pandas as pd

def categorize_products(a: pd.DataFrame) -> pd.DataFrame:

    dicts = {}

    for indx, r in a.iterrows():
        if str(r['sell_date']) in dicts:
            dicts[str(r['sell_date'])].add(r['product'])
        else:
            dicts[str(r['sell_date'])] = {r['product']}

    for x in dicts:
        dicts[x] = list(dicts[x])
        dicts[x].sort()

    ans_rows = []
    ans_cols = ['sell_date','num_sold','products']

    for x in dicts:
        ans_rows.append([x[:10], len(dicts[x]), ','.join(dicts[x])])

    ans_rows = sorted(ans_rows, key = lambda x:x[0])
    return pd.DataFrame(data=ans_rows, columns=ans_cols)
