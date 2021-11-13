class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        lastreached = len(nums)-1
        
        for x in range(len(nums)-2,-1,-1):
            if x+nums[x]>=lastreached:
                lastreached = x
                
                
        if lastreached == 0:
            return True
        
        else:
            return False
          
          
 ## Similar to DP Approach, the only difference is rather than keeping the whole dp array, we keep a track of last index that could have been reached traversing the nums array backwards
