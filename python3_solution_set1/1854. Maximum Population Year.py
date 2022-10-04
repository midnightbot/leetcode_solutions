##ss
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        years = {x:0 for x in range(1950,2051)}
        
        for s,e in logs:
            for y in range(s,e):
                years[y]+=1
                
                
        maxs = max(years.values())
        for y in years:
            if years[y] == maxs:
                return y
        
