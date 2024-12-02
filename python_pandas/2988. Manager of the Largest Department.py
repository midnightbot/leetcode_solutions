import pandas as pd

def find_manager(employees: pd.DataFrame) -> pd.DataFrame:

    manager = {}
    dept = {}

    for indx, r in employees.iterrows():
        dept[r['dep_id']] = dept.get(r['dep_id'],0) + 1
        if r['position'] == 'Manager':
            manager[r['dep_id']] = r['emp_name']

    maxs = max(dept.values())
    depts = []

    for x in dept:
        if dept[x] == maxs:
            depts.append(x)

    depts = sorted(depts)
    ans = []
    cols = ['manager_name','dep_id']

    for d in depts:
        ans.append([manager[d],d])

    return pd.DataFrame(data=ans, columns=cols)
    
