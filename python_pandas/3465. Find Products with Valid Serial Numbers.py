import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    ans = []
    ans_cols = ['product_id', 'product_name', 'description']
    pattern = r"^SN\d{4}-\d{4}$"
    for indx, r in products.iterrows():
        words = r['description'].split(" ")
        present = False
        for x in words:
            if bool(re.match(pattern, x)):
                present = True
                break

        if present:
            ans.append(r)


    return pd.DataFrame(columns=ans_cols, data=ans)
    
    
