class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        ans = []
        for x in range(0,len(nums),2):
            ans.append(nums[x+1])
            ans.append(nums[x])
            
        return ans
        
