##ss
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        ans = 0
        
        nums = sorted(nums)
        
        check = {}
        for x in range(len(nums)):
            if nums[x] in check:
                check[nums[x]]+=1
                
            else:
                check[nums[x]] = 1
                
        for x in check:
            if k >0 and x+k in check:
                ans+=1
                
            elif k==0 and check[x] > 1:
                ans+=1
                
        return ans
        
