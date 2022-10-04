class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        
        while left <=right:
            middle = (left+right) // 2
            
            if nums[middle] == target:
                return middle
            
            elif target < nums[middle]:
                right = middle - 1
                
            else:
                left = middle + 1
                
        return left
        
        
        
        
