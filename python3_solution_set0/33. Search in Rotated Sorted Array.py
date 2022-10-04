class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        ##logn complexity -> clear indication to use binary search
        
        ans = -1
        
        ##but how to use binary search , as array is not sorted
        ##can think it of as two seperate arrays
        ##just need to find the split index
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            
            if nums[mid] == target: ##element found return the index
                return mid
            
            elif nums[mid] >= nums[left]: ## there is no split from left .. mid, as it is in sorted order no disruption
                if target >= nums[left] and target < nums[mid]:##target is between the first half of list
                    right = mid - 1
                    
                else: ## target is in the second half of the list
                    left = mid + 1
                    
            else:
                if target >= nums[mid] and target<=nums[right]:
                    left = mid + 1
                    
                else:
                    right = mid - 1
                    
                    
        return ans
                
                
        
        
