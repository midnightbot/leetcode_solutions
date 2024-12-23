class Solution:
    def is_unique(self, arr):
        return len(arr) == len(set(arr))

    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        not_done = True

        while not_done:
            if self.is_unique(nums):
                return ans

            for x in range(min(3, len(nums))):
                nums = nums[1:]
            ans+=1
        return ans
        
