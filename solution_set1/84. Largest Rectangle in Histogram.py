class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        area = 0
        stack = []
        
        for x in range(len(heights)):
            start = x
            
            while stack and stack[-1][1] > heights[x]:
                index,ht = stack.pop()
                area = max(area, ht * (x-index))
                
                start = index
                
            stack.append([start,heights[x]])
            
        for x in stack:
            area = max(area,x[1] * (len(heights)-x[0]))
        
        return area
        
