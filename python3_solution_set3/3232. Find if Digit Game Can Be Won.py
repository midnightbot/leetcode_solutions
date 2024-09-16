class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        nums.sort()
        print(nums)
        indx = bisect.bisect_left(nums, 10)
        # print(indx)
        # a = sum(nums[:indx])
        # b = sum(nums[indx:])
        # print(a,b)
        return sum(nums[:indx]) != sum(nums[indx:])


        
