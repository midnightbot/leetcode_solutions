##ss
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        for x in range(1,len(arr)):
            arr[x]+=arr[x-1]
        arr.insert(0,0) 
        ans  = 0
        for x in range(len(arr)):
            for y in range(x+1,len(arr),2):
                ans+=arr[y]  - arr[x]
                
        return ans
                
        
