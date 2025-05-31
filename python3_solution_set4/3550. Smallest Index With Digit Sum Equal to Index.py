class Solution:
    def find_sum(self, num):
        return sum([int(x) for x in str(num)])

    def smallestIndex(self, nums: List[int]) -> int:

        for x in range(len(nums)):
            if x == self.find_sum(nums[x]):
                return x

        return -1
        
