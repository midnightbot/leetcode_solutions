##ss
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        dicts = {}
        ans = set()
        for x in range(len(nums)):
            ans.add(x+1)
            
        result = [-1,-1]
        for x in range(len(nums)):
            if nums[x] in dicts:
                result[0] = nums[x]
                dicts[nums[x]]+=1
                
            else:
                dicts[nums[x]] = 1
                ans.remove(nums[x])
                
                
        result[1] = list(ans)[0]
        return result
                
        
            
            
        
