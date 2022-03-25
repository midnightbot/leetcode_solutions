##ss
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        c = 0
        sums  = sum(arr[:k])
        
        if sums / k >= threshold:
            c+=1
            
        for x in range(len(arr)-k):
            sums-=arr[x]
            sums+=arr[k+x]
            
            if sums / k >= threshold:
                c+=1
                
        return c
        
