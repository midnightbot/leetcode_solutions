class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        
        for x in range(len(arr)):
            if arr[x] == x:
                return x
            
            
        return -1
        
