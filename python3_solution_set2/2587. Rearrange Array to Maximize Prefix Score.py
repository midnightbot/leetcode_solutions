class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)

        cnt = list(accumulate(nums))

        

        return sum([1 if x>0 else 0 for x in cnt])
