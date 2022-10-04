##ss
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        ##simple bfs
        
        visited = set()
        ans = 0
        
        q = initialBoxes
        
        for bxs in q:
            ans+=candies[bxs]
            
            for x in containedBoxes[bxs]:
                if status[x] == 1:
                    q.append(x)
                    
                    
                visited.add(x)
                
                
            for x in keys[bxs]:
                if status[x] == 0 and x in visited:
                    q.append(x)
                status[x] = 1
        
        return ans
        
