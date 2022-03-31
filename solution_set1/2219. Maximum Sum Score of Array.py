##ss
class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        
        arr1 = []
        arr2 = []
        sums = 0
        for x in range(len(nums)):
            sums+=nums[x]
            arr1.append(sums)
        
        sums = 0
        for x in range(len(nums)-1,-1,-1):
            sums+=nums[x]
            arr2.append(sums)
            
        arr2 = arr2[::-1]
        
        res = -float('inf')
        for x in range(len(arr1)):
            res = max(res,arr1[x],arr2[x])
            
        return res
