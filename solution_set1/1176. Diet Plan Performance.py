##ss
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        
        sums = sum(calories[0:k])
        pts = 0
        if sums < lower:
            pts-=1
            
        elif sums > upper:
            pts+=1
            
        for x in range(len(calories)-k):
            sums-=calories[x]
            sums+=calories[x+k]
            
            if sums < lower:
                pts-=1
            
            elif sums > upper:
                pts+=1
            
        return pts
            
        
