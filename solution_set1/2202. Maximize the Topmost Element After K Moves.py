
###ss
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        
        
        if len(nums) == 1 and k%2==0:
            return nums[0]
        
        elif len(nums) == 1 and k%2!=0:
            return -1
        
        elif k - 1 == nums.index(max(nums[0:k+1])):
            temp = nums[0:k+1]
            temp = sorted(temp)
            
            return temp[-2]
        
        elif len(nums) == k:
            
            temp = sorted(nums)
            
            i = nums.index(temp[-1])
            
            if (k - i - 1) % 2 == 0:
                return temp[-1]
            else:
                return temp[-2]
        
        
        
        
        elif k < len(nums):
            return max(nums[0:k+1])
        
        elif k > len(nums):
            return max(nums)
        
        
        
        
