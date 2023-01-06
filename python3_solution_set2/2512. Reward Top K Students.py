class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:

        n = len(report)
        points = {}

        pos = set(positive_feedback)
        neg = set(negative_feedback)

        for x in range(n):
            sen = report[x]
            temp = sen.split(" ")
            score = 0

            for its in temp:
                if its in pos:
                    score+=3
                if its in neg:
                    score-=1

            points[student_id[x]] = score
        points = [(points[x],x) for x in points]
        points = sorted(points, key = lambda x:(-x[0],x[1]))
        #print(points)
        return [x[1] for x in points][:k]
