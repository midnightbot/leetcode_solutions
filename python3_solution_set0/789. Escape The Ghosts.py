##ss
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        ##if my shortest path to target < ghost shortest path to target   (I will always reach target without getting caught)
        
        for x in range(len(ghosts)):
            if self.count_moves([0,0],target) >= self.count_moves(ghosts[x],target):
                return False
            
        return True
        
    def count_moves(self,start,end):
        
        return abs(start[0]-end[0]) + abs(start[1]-end[1])
        
