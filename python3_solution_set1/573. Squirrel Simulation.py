##ss
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        

        ##squirrel will go to the nut whose dist from tree is max
        
        total = 0
        overlap = -float('inf')
        
        for x in range(len(nuts)):
            total+=self.calc_dist(nuts[x],tree) * 2
            
            overlap = max(overlap, self.calc_dist(nuts[x],tree) - self.calc_dist(nuts[x],squirrel))
            
        return total - overlap
        
        
    def calc_dist(self,p1,p2):
        
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
