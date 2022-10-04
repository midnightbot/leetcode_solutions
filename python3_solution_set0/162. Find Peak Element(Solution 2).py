##ss
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        ##logn, hint  to use binary search
        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return nums.index(max(nums))
        while left < right:
            mid = left +(right - left ) // 2
            
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid+1] and mid-1<0:
                return mid
            elif nums[mid] > nums[mid - 1] and mid + 1 > len(nums):
                return mid
            
            elif nums[mid] < nums[mid - 1]:
                right = mid
                
            else:
                left = mid + 1
                
        return right
        
