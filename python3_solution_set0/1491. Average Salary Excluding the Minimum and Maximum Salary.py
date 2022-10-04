class Solution:
    def average(self, salary: List[int]) -> float:
        
        salary = sorted(salary)
        sums = 0
        for x in range(1,len(salary)-1):
            sums +=salary[x]
            
        return sums/(len(salary)-2)
        
