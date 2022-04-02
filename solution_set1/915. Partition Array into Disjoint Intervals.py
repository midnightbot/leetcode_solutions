##ss
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        
        ## left and right
        ## all[right] >= all[left]
        ##left is min
        
        maxs = []
        mins = []
        maxs.append(nums[0])
        
        for x in range(1,len(nums)):
            maxs.append(max(maxs[-1],nums[x]))
            
        mins.append(nums[-1])
        
        for x in range(len(nums)-2,-1,-1):
            mins.append(min(mins[-1],nums[x]))
            
        mins = mins[::-1]
        #print(maxs)
        #print(mins)
        for x in range(len(maxs)):
            if maxs[x] <= mins[x+1]:
                return x+1
            
            
        
