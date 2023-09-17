class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        og_nums = nums
        nums = nums + nums

        for x in range(0,len(og_nums)):
            arr = nums[x:x+len(og_nums)]
            #print(arr)
            if arr == sorted(arr):
                return (len(og_nums) - x)%len(og_nums)

        return -1
        
