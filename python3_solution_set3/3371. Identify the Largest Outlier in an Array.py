class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        sums = sum(nums)
        temp = set(nums)
        ans = -float('inf')
        maps = {}
        # print(sums)
        for i,x in enumerate(nums):
            maps[x] = maps.get(x,0) + 1

        for i,x in enumerate(nums):
            rem = sums - x
            if rem/2 in temp:
                if rem/2 != x:
                    ans = max(ans, x)
                else:
                    # print(x, maps)
                    if maps[x] >1:
                        ans = max(ans, x)

        return ans

        
