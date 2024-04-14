class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        return sum([int(str(max([int(z) for z in str(i)]))*len(str(i))) for i in nums])
        
