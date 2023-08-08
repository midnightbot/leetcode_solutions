import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    imm = 0
    sch = 0

    for indx, r in delivery.iterrows():
        if r['order_date'] == r['customer_pref_delivery_date']:
            imm+=1
        else:
            sch+=1

    ans_rows = [round((imm/(imm+sch))*100,2)]
    return pd.DataFrame(data=ans_rows, columns=['immediate_percentage'])
