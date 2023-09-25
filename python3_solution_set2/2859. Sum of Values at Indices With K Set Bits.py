class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:

        def bit_count(x):
            temp = format(x,'b')
            return temp.count('1')

        ans = 0
        for indx, x in enumerate(nums):
            if bit_count(indx) == k:
                ans+=x

        return ans
        
