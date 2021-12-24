##ss
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        ans = []
        
        for x in range(len(nums)):
            ans.append(a*nums[x]**2 + b*nums[x]+c)
            
        ans = sorted(ans)
        
        return ans
        
