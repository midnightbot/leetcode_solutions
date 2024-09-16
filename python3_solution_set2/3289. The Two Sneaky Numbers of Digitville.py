class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()

        for x in range(len(nums)-1):
            if nums[x] == nums[x+1]:
                ans.append(nums[x])
        return ans
        
