import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:

    def conv(x):
        return int(x)

    students['grade'] = students['grade'].apply(conv)
    return students
    
