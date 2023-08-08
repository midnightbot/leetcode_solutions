import pandas as pd

def total_time(e: pd.DataFrame) -> pd.DataFrame:

    e['total_time'] = e['out_time'] - e['in_time']
    e = e.groupby(['event_day', 'emp_id'], as_index = False).agg(sum)
    e = e.rename(columns={'event_day':'day'})
    return e.drop(columns=['in_time','out_time'])
    
