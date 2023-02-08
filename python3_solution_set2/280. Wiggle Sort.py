class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## if i%2==0 nums[i] <= nums[i+1]
        ## else nums[i] >= nums[i+1]

        for i in range(len(nums)-1):
            if i%2==0 and nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1], nums[i]

            if i%2!=0 and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
