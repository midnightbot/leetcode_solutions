class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        first = -1
        last = -1
        
        start = 0
        end = len(nums) -1
        
        while start <= end: ## finding the first position of number
            ##if for nums[mid] == target, then first postion will be either mid or less than mid
            mid = start + (end-start)//2
            
            if nums[mid] == target:
                first = mid
                end = mid - 1
                
            elif nums[mid] > target:
                end = mid - 1
                
            else:
                start = mid + 1
                
        start = 0
        end = len(nums) -1        
        while start <= end: ## finding last position of the target
            ## if nums[mid] == target, then last position will be either mid or greater than mid
            mid = start + (end-start)//2
            
            if nums[mid] == target:
                last = mid
                start = mid + 1
                
            elif nums[mid] > target:
                end = mid - 1
                
            else:
                start = mid + 1
                
        return [first, last]
        
