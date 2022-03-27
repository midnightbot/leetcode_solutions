##ss
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        pairs = 0
        seen = {}
        for x in range(len(nums)):
            if k - nums[x] in seen:
                seen[k-nums[x]]-=1
                pairs+=1
                
                if seen[k-nums[x]] == 0:
                    seen.pop(k-nums[x])
                    
            else:
                seen[nums[x]] = seen.get(nums[x],0) + 1
                
                
        return pairs
        
