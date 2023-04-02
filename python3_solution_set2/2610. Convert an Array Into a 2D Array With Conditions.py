class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        temp = Counter(nums)
        maxs = max(list(temp.values()))

        ans = []
        for x in range(maxs):
            r = []
            for it in temp:
                if temp[it]!=0:
                    r.append(it)
                    temp[it]-=1
            ans.append(r)
        return ans
