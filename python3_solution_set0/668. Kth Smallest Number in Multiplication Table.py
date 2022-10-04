class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left = 1
        right = m*n
        while left < right:
            mid = int(left + int(((right-left)/2)))
            if self.freq(mid,m,n,k):
                right = mid
            else:
                left = mid + 1
                
        return left
        
        
    def freq(self,num,m,n,k):
        count = 0
        for i in range(1,m+1):
            count+=min(num//i,n)
            
        return count>=k
        
