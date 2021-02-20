class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        
        for x in range(len(nums)):
            digits = [int(z) for z in str(nums[x])]
            if(len(digits)%2==0):
                count+=1
                
        return count
        
