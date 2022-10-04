class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        temp = []
        
        
        while len(nums)!=1:
            op = 1
            temp = []
            for x in range(0,len(nums),+2):
                
                if op == 1:
                    temp.append(min(nums[x],nums[x+1]))
                    op = 2
                    
                else:
                    temp.append(max(nums[x],nums[x+1]))
                    op = 1
                    
            nums = temp
            
        return nums[0]
