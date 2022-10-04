class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        
        mins = []
        temp =0 
        for x in range(len(nums)):
            temp+=nums[x]
            mins.append(temp)
            
        mini = min(mins)
        
        if mini>0:
            return 1
        else:
            return (-mini+1)
            
        
