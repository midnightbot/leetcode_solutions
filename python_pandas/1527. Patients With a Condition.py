import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:

    ans = []

    def valid(str):
        temp = str.split(' ')
        for it in temp:
            if len(it) >=5 and it[:5] == 'DIAB1':
                return True

        return False

    for indx, r in patients.iterrows():
        if valid(r['conditions']):
            ans.append(indx)

        
    return patients.loc[ans]
