import pandas as pd

def largest_orders(o: pd.DataFrame) -> pd.DataFrame:
    return o['customer_number'].mode().to_frame()
