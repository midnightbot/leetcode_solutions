##ss
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        lsum = 0
        rsum = sum(nums[1:])
        
        for x in range(len(nums)-1):
            if lsum == rsum:
                return x
            
            lsum+=nums[x]
            rsum-=nums[x+1]
            
            
        lsum = sum(nums[0:len(nums)-1])
        rsum = 0
        #print(lsum)
        if lsum == rsum:
            return len(nums)-1
        
        else:
            return -1
        
