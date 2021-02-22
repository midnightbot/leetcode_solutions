class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        maxs = []
        satisfaction.sort()
        sums = 0
        
        for x in range(len(satisfaction)):
            sums = 0
            for y in range(x):
                sums = sums + satisfaction[y]*(y+1)
            
            maxs.append(sums)
            sums=0
            
            for z in range(x,len(satisfaction)):
                sums = sums + satisfaction[z]*(z+1-x)
                
            
            
            maxs.append(sums)
            
        return max(maxs)
                
        
