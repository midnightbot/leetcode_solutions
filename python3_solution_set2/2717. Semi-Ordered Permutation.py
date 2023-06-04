class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:

        indx1 = nums.index(1)
        indx2 = nums.index(len(nums))
        n = len(nums)

        if indx1 < indx2:
            return indx1 + (n - indx2 - 1)

        else:
            diff = abs(indx1 - indx2)
            return indx1 + (n - indx2 - 2)
        
