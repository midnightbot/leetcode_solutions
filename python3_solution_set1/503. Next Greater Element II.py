##ss
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        nums = nums + nums + nums
        
        result = []
        
        for x in range(n,2*n,1):
            done = False
            for y in range(x+1,x+n+1):
                
                if nums[y] > nums[x]:
                    done = True
                    result.append(nums[y])
                    break
                    
            if done == False:
                result.append(-1)
                
        return result
        
