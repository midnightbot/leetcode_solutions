class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        ## change stack[-1] to a lower number , i.e current number
        ## or change current number to stack[-1]
        c = 0
        for x in range(len(nums)-1):
            if nums[x] > nums[x+1]:
                c+=1
                
                if x == 0:
                    nums[x] = nums[x+1]
                    
                elif nums[x-1] <= nums[x+1]:
                    nums[x] = nums[x-1]
                    
                else:
                    nums[x+1] = nums[x]
                    
                    
            if c > 1:
                return False
        
        
        return True
                    
            
