class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ans = []
        visited  = []
        for x in range(len(nums)):
            if nums[x] not in visited:
                visited.append(nums[x])
                
                ans.append((nums.count(nums[x]),nums[x]))
                
                
        ans = sorted(ans,reverse=True)
        final = []
        
        for x in range(k):
            final.append(ans[x][1])
            
        return final
