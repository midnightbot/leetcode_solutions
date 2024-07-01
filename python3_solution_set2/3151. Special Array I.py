class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        nums = [nums[x]%2 for x in range(len(nums))]
        seq1 = [0 for x in range(len(nums))]
        seq2 = [1 for x in range(len(nums))]
        for x in range(len(nums)):
            if x%2==0:
                seq1[x]=1
                seq2[x]=0
        return nums==seq1 or nums==seq2
        
