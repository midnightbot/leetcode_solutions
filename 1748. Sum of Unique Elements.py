class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        current = 0
        sums = 0
        tt = 0
        for x in range(len(nums)):
            current = nums[x]
            tt=0
            for y in range(len(nums)):
                if x!=y and current==nums[y]:
                    tt+=1
                    
            if tt==0:
                sums+=nums[x]
                
        return sums
                    
        
