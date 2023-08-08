import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:

    c = courses.groupby('class',as_index=False).count()
    return c[c['student']>=5][['class']]
