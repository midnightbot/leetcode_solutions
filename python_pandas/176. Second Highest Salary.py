import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset='salary')
    employee = employee.sort_values(by='salary', ascending=False)
    employee  = employee.reset_index(drop=True)
    ans_cols = ['SecondHighestSalary']
    if len(employee) < 2:
        ans_rows = [None]

    else:
        ans_rows = [employee.loc[1]['salary']]

    return pd.DataFrame(data=ans_rows, columns = ans_cols)
