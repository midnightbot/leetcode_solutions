##ss
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        ans = 0
        for x in range(len(nums)-1):
            for y in range(x+1,len(nums)):
                if nums[x] == nums[y] and (x*y)%k==0:
                    ans+=1
                
        return ans
        
        
        
