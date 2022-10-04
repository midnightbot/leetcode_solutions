class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = 0
        ans=[]
        for x in range(len(nums)):
            sums+=nums[x]
            ans.append(sums)
            
        return ans
