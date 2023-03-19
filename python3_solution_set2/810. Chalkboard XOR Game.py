class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        xor = 0
        for x in nums:
            xor^=x

        return xor==0 or len(nums)%2==0
