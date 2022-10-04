##ss
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        ans = []
        fwd = sum(nums)
        back = 0
        
        for x in range(len(nums)):
            back+=nums[x]
            fwd-=nums[x]
            #print(back,fwd)
            ans.append(abs(back-nums[x]*(x-0+1))+abs(fwd-nums[x]*(len(nums)-x-1)))
            
        return ans
        
