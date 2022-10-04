##ss
##prefix sum
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        prefix = [0]
        
        count = 0
        for x in range(len(nums)):
            if nums[x] == 0:
                count+=1
                
            prefix.append(count)
            
        suffix = [0]
        count = 0
        for x in range(len(nums)-1,-1,-1):
            if nums[x] == 1:
                count+=1
                
            suffix.append(count)
        suffix = suffix[::-1]
        ans = []
        maxs = -1
        for x in range(len(prefix)):
            #print(prefix[x],suffix[x])
            if prefix[x]+suffix[x] > maxs:
                maxs = prefix[x]+suffix[x]
                ans = [x]
                
            elif prefix[x]+suffix[x] ==maxs:
                ans.append(x)
                
        return ans
        
