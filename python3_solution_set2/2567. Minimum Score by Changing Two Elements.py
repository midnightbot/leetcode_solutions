class Solution:
    def minimizeSum(self, nums: List[int]) -> int:

        ## score = high + low
        ## minimize score by changing at most two values in nums

        ## to minimize score we have to minimize high and low

        ## if two elements in nums are same then low = 0 (will make low always 0)

        ## hence try to make two elements same (atmost 1 operation)

        ## 3 choice, change ff, ll, fl

        nums.sort()
        option1 = nums[-1] - nums[2]
        option2 = nums[-3] - nums[0]
        option3 = nums[-2] - nums[1]

        return min(option1, option2, option3)
