##ss
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        
        ##3 mins changed
        ##3 maxs changed
        ##2 mins 1 maxs changed
        ##2maxs 1 mins changed
        
        nums = sorted(nums)
        
        if len(nums) <= 4:
            return 0
        
        else:

            ans1 = nums[len(nums)-1]-nums[3]
            ans2 = nums[len(nums)-2] - nums[2]
            ans3 = nums[len(nums)-3] - nums[1]
            ans4 = nums[len(nums)-4] - nums[0]
            
            return min(ans1,ans2,ans3,ans4)
        
