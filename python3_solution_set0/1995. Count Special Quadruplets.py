class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        
        ans = 0
        
        for x in range(len(nums)-3):
            for y in range(x+1,len(nums)-2):
                for z in range(y+1,len(nums)-1):
                    for k in range(z+1,len(nums)):
                        if nums[x]+nums[y] +nums[z]== nums[k]:
                            ans+=1
                            
                            
        return ans
        
