##ss
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        
        diff = arr[-1] - arr[0]
        
        p = diff // (len(arr))
        
        for x in range(1,len(arr)):
            if arr[x] != arr[x-1] + p:
                return int(arr[x-1] + p)
        
        return arr[0] ##if all numbers are same
