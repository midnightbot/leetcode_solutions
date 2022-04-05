##ss
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def can_do(pen):
            c = 0
            
            for x in nums:
                c+=(x-1)//pen
                
            #print(pen,c)
            return c > maxOperations
        
        
        left = 1
        right = max(nums)
        
        while left < right:
            mid = (left + right) // 2
            #print(mid)
            if can_do(mid):
                left = mid + 1
                
            else:
                right = mid
                
        return left
        
