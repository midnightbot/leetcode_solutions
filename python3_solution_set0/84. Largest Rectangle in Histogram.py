##Solution 1(Time Limit Exceeded)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
 
        ans = 0
        for x in range(len(heights)):
            hts = float('inf')
            for y in range(x,len(heights)):

                hts = min(hts, heights[y])
                ans = max(ans, (y-x+1)*hts)

               
                    
        print(ans)
        return max(ans,max(heights))
      
## Solution 2
