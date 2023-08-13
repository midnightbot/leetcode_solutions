class Solution:
    def maxSum(self, nums: List[int]) -> int:

        dicts = defaultdict(list)
        ans = -1
        for x in nums:
            temp = [int(i) for i in str(x)]
            temp = max(temp)
            dicts[temp].append(x)

        for i in dicts:
            arr = dicts[i]
            arr.sort()
            if len(arr) >= 2:
                ans = max(ans, arr[-1] + arr[-2])

        return ans
