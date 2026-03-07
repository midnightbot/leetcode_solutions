class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min([(x[0]+x[1]) for x in tasks])
        
