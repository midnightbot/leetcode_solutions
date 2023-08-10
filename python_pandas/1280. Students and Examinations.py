import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    examinations = examinations.groupby(['student_id','subject_name']).agg(attended_exams=('subject_name','count')).reset_index()

    students = students.merge(subjects,how='cross')

    examinations = examinations.merge(students, on=['student_id','subject_name'],how='right')

    examinations = examinations.fillna(0)
    examinations = examinations.sort_values(['student_id','subject_name'])
    return examinations[['student_id','student_name','subject_name','attended_exams']]
