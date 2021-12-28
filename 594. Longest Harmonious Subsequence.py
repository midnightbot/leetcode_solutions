##ss
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        dicts = {}
        nums = sorted(nums)
        ans = 0
        for x in range(len(nums)):
            if nums[x] in dicts.keys():
                dicts[nums[x]]+=1
                
                
            else:
                dicts[nums[x]] = 1
                
        #print(dicts)   
        prev = - float('inf')
        for x in dicts.keys():
            if x == prev+1:
                ans = max(ans, dicts[x] + dicts[prev])
                
            prev = x
            
        return ans
