class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        heights_ordered = sorted(heights)
        count = 0
        for x in range(len(heights)):
            if heights[x]!=heights_ordered[x]:
                count+=1
                
        return count
        
