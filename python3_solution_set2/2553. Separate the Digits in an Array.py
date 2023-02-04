class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        ans = []

        for it in nums:
            for l in str(it):
                ans.append(l)
        ans = [int(x) for x in ans]
        return ans
