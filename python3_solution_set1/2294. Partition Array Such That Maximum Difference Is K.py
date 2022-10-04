class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)
        
        ans = 1
        
        curr = nums[0]
        for x in range(len(nums)):
            
            if nums[x] - curr <= k:
                continue
            else:
                curr = nums[x]
                ans+=1
                
        return ans
        
