##ss
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        ##can be done in O(N)
        ##we just need smallest 2 numbers and largest 3 numbers
        nums = sorted(nums)
        
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
        
