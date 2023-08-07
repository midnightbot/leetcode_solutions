import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:

    ans_rows = set()
    ans_cols = ['id']

    for indx, r in views.iterrows():
        if r['author_id'] == r['viewer_id']:
            ans_rows.add(r['author_id'])

    ans_rows = sorted(list(ans_rows))
    return pd.DataFrame(data=(ans_rows), columns = ans_cols)
