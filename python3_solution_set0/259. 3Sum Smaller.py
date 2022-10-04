##ss
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = 0
        
        for x in range(len(nums)-2):
            ans+= self.twosum(x+1,len(nums)-1,nums,target-nums[x])
            
        return ans
        
        
        
        
    def twosum(self,i,j,nums,target):
        
        
        ans = 0
        while i < j:
            if nums[i] + nums[j] < target:
                ans+= j - i
                i+=1
            else:
                j-=1
                
        return ans
        
