##ss
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        if len(nums) == 0:
            if upper == lower:
                return [str(upper)]
            else:
                return [str(lower)+"->"+str(upper)]
        ans = []
        if nums[0] > lower:
            if nums[0] - lower == 1:
                ans.append(str(lower))
                
            elif nums[0] - lower >= 2:
                ans.append(str(lower)+"->"+str(nums[0]-1))
            
        #print(ans)
        for x in range(1,len(nums)):
            
            temp = nums[x] - nums[x-1]
            
            if temp ==2:
                ans.append(str(nums[x-1]+1))
                
            elif temp > 2:
                ans.append(str(nums[x-1]+1)+"->"+str(nums[x]-1))
                
            #print(ans)
            
        if nums[-1] < upper:
            if upper - nums[-1] == 1:
                ans.append(str(upper))
                
            elif upper - nums[-1] >= 2:
                ans.append(str(nums[-1]+1)+"->"+str(upper))
                
        return ans
        
