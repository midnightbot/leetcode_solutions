import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:

    ans =  teacher.groupby('teacher_id').nunique().reset_index()
    ans = ans.drop(columns = ['dept_id'])
    ans = ans.rename(columns={'subject_id':'cnt'})
    return ans
