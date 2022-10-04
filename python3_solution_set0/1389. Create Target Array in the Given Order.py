class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        a = []
        for x in range(len(nums)):
            a.insert(index[x],nums[x])
            
        return a
