class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        for x in range(len(nums)):
            temp = nums[x]
            ans.append(nums[temp])
            
        return ans
