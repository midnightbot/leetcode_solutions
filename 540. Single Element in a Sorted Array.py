class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        
        elif nums[0]!=nums[1]:
            return nums[0]
        
        elif nums[len(nums)-1]!=nums[len(nums)-2]:
            return nums[len(nums)-1]
        while left < right:
            
            mid = left + (right-left)//2
            print(mid)   
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            
            elif mid%2!=0 and nums[mid]!=nums[mid-1] and nums[mid] == nums[mid+1]:
                
                right = mid
            elif mid%2!=0 and nums[mid]==nums[mid-1]:
                left = mid
            
            elif mid%2 == 0 and nums[mid]!=nums[mid+1]:
                right = mid
            elif mid%2 == 0 and nums[mid]==nums[mid+1]:
                left = mid
               
        
        
        ##idea element at even index is the new element
        ##element at odd index is same as the prev element
        
        ##if while doing binary search we land on odd index and its value is not equal to prev bu value equal to next element, we know that unique element will be on the left side as it distorted the even odd order
            
            
            
            
        
