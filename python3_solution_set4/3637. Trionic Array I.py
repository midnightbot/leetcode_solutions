class Solution:
    def is_inc(self, arr):
        for x in range(len(arr)-1):
            if arr[x] >= arr[x+1]:
                return False
        return True

    def is_dec(self, arr):
        for x in range(len(arr)-1):
            if arr[x] <= arr[x+1]:
                return False
        return True

    def isTrionic(self, nums: List[int]) -> bool:
        
        for i in range(1,len(nums)-2):
            for j in range(i+1, len(nums)-1):
                arr1 = nums[:i+1]
                arr2 = nums[i:j+1]
                arr3 = nums[j:]
                # print(arr1, arr2, arr3)
                if self.is_inc(arr1) and self.is_dec(arr2) and self.is_inc(arr3):
                    return True

        return False

        
