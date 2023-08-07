import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:

    ans_cols = ['product_id','store','price']
    ans_rows = []

    for indx, r in products.iterrows():
        if pd.notna(r['store1']):
            ans_rows.append([r['product_id'], 'store1',r['store1']])

        if pd.notna(r['store2']):
            ans_rows.append([r['product_id'], 'store2',r['store2']])

        if pd.notna(r['store3']):
            ans_rows.append([r['product_id'], 'store3',r['store3']])

    return pd.DataFrame(data=ans_rows, columns = ans_cols)
