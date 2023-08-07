import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    employees['bonus'] = 0

    for indx, r in employees.iterrows():
        if r['employee_id']%2!=0 and r['name'][0]!='M':
            employees.loc[indx,'bonus'] = r['salary']

    employees = employees.sort_values(by='employee_id')
    return employees[['employee_id','bonus']]
