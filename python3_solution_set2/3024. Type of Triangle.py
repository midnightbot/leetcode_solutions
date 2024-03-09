class Solution:
    def triangleType(self, nums: List[int]) -> str:
        ## sum of any two sides greater than third
        if (nums[0] + nums[1] <= nums[2]) or (nums[1] + nums[2] <= nums[0]) or (nums[0] + nums[2] <= nums[1]):
            return "none"
        if len(nums) == len(set(nums)):
            return "scalene"

        elif len(set(nums)) == 2:
            return "isosceles"

        else:
            return "equilateral"
        
