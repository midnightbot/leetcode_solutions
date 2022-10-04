class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        ans = []
        
        maxs = heights[len(heights)-1]
        ans.append(len(heights)-1)
        for x in range(len(heights)-2,-1,-1):
            if heights[x] > maxs:
                ans.append(x)
                maxs = heights[x]
                
            
                
        return ans[::-1]
            
        
        
        
        
