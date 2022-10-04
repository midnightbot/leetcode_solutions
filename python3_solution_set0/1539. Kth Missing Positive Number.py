##ss
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        if arr[0] - 1 >= k:
            return k
        
        k-=arr[0] -1 
        
        for x in range(len(arr)-1):
            
            temp = arr[x+1] - arr[x] - 1
            
            if temp>=k:
                return arr[x] + k
            
            k-=temp
            
        return arr[len(arr)-1] + k
        
