class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        
        for x in range(0,len(nums)-1,2):
            for y in range(nums[x]):
                ans.append(nums[x+1])
                
                
        return ans
            
        
