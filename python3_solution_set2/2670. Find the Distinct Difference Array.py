class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for x in range(n):
            set1 = set(nums[0:x+1])
            set2 = set(nums[x+1:])

            ans.append(len(set1) - len(set2))

        return ans
