##ss
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        less = []
        equal = []
        big = []
        
        for x in range(len(nums)):
            if nums[x] < pivot:
                less.append(nums[x])
                
            elif nums[x] == pivot:
                equal.append(nums[x])
                
            else:
                big.append(nums[x])
                
        return less + equal + big
        
