import pandas as pd
def is_ok(s):
    ans = []
    curr = 0
    for x in s:
        if x in '1234567890':
            curr+=1
        else:
            ans.append(curr)
            curr = 0
    ans.append(curr)
    # print(ans)
    return 3 in ans

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    ans_rows = []
    ans_cols = ['product_id', 'name']

    for indx, r in products.iterrows():
        if is_ok(r['name']):
            ans_rows.append([r['product_id'],r['name']])
    
    print(ans_rows)
    return pd.DataFrame(data=ans_rows, columns=ans_cols)
    
