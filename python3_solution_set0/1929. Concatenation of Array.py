class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        
        ans = []
        for x in range(len(nums)):
            ans.append(nums[x])
            
            
        for y in range(len(nums)):
            ans.append(nums[y])
            
            
        return ans
        
