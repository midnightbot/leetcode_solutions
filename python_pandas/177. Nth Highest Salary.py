import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    employee = employee['salary'].drop_duplicates()

    employee = employee.sort_values(ascending=False)

    if len(employee) < N:
        return pd.DataFrame({'Nth Highest Salary': [None]})

    return pd.DataFrame({'Nth Highest Salary': [employee.iloc[N-1]]})

    
