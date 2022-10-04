##ss
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        
        indices = []
        
        for x in range(len(nums)):
            if nums[x] == key:
                indices.append(x)
                
        ans = set()
        for x in range(len(indices)):
            ##behind
            for y in range(indices[x],max(indices[x] - k-1, -1), -1):
                ans.add(y)
                
            for y in range(indices[x], min(indices[x]+k+1, len(nums))):
                ans.add(y)
                
                
        ans = sorted(list(ans))
        return ans
        
