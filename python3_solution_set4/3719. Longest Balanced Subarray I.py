class Solution:
    def longestBalanced(self, nums: List[int]) -> int:

        ans = 0

        for x in range(len(nums)):
            odd = {}
            even = {}

            for y in range(x, len(nums)):
                if nums[y]%2!=0:
                    odd[nums[y]] = odd.get(nums[y],0)+1
                else:
                    even[nums[y]] = even.get(nums[y],0)+1
                if len(odd) == len(even):
                    ans = max(ans, y-x+1)
        return ans
        
