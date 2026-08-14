class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            if x%2==0:
                ans|=x

        return ans
        
