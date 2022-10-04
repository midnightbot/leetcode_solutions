class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        
        ## all local inv are also global inv
        
        for x in range(len(nums)):
            if abs(nums[x]-x) > 1 :
                return False
            
        return True
        #return all(abs(nums[x]-x)<=1 for x in range(len(nums)))
        
