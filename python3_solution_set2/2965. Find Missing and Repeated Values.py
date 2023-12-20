class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr = []
        for x in grid:
            arr+=x
        temp = Counter(arr)
        ans = []

        for x in range(1, (len(grid)**2)+1):
            if x not in temp:
                ans.append(x)

        for x in temp:
            if temp[x] == 2:
                ans.append(x)

        return ans[::-1]
