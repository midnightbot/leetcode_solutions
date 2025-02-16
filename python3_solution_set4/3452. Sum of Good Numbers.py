class Solution:
    def find_maxs(self, indx, k):
        arr = []
        if indx - k >=0:
            arr.append(self.nums[indx-k])
        if indx + k < self.n:
            arr.append(self.nums[indx+k])
        
        if arr:
            return max(arr)
        return -float('inf')
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.n = len(self.nums)
        ans = 0

        for x in range(self.n):
            i = self.find_maxs(x,k)
            if i < self.nums[x]:
                ans+=self.nums[x]
        return ans
        
