class Solution:
    def is_ok(self, arr):

        for x in range(1, len(arr)):
            if arr[x] < arr[x-1]:
                return False
        return True

    def update_arr(self, arr):
        sums = []

        for x in range(1, len(arr)):
            sums.append(arr[x] + arr[x-1])
        
        mins = sums.index(min(sums))
        ## replace mins, mins+1 by it sum

        arr = arr[0:mins] + [arr[mins] + arr[mins+1]] + arr[mins+2:]
        return arr

    def minimumPairRemoval(self, nums: List[int]) -> int:

        ans = 0
        while not self.is_ok(nums):
            nums = self.update_arr(nums)
            ans+=1

        return ans
        
