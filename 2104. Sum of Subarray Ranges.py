##ss
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        ans = []
        temp =  len(nums)
        for x in range(len(nums)-1):
            self.combinations(nums,x,nums[x],nums[x],ans,temp)
        return sum(ans)
    def combinations(self,nums,i,mins,maxs,ans,temp):
        
        if len(nums) == 0 or i >= temp:
            ans.append(maxs-mins)
            
        else:
            self.combinations(nums,i+1,min(mins,nums[i]),max(maxs,nums[i]),ans,temp)
            self.combinations([],-1,mins,maxs,ans,temp)
    
    
        
