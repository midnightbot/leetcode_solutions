class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        maxs = arr[0]
        anss = 0
        for x in range(len(arr)):
            if arr[x] > maxs:
                maxs = arr[x]
                anss = x
                
        return anss
            
        
