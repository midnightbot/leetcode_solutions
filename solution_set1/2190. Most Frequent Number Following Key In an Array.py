##ss
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        
        maxs = -1
        ans = -1
        comp = {}
        
        for x in range(len(nums)-1):
            
            if nums[x] == key:
                comp[nums[x+1]] = comp.get(nums[x+1],0) + 1
                
                if comp[nums[x+1]] > maxs:
                    maxs = comp[nums[x+1]]
                    ans = nums[x+1]
                    
        return ans
                
        
