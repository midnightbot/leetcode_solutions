class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        ## no  ne
        #print(3 ^ 2 ^ 4 ^ 2)
        
        ans = nums[0]
        for x in nums[1:]:
            ans|=x
            
        return ans
