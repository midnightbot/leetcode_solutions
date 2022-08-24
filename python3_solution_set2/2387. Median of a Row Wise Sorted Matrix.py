class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        arr = []
        for x in grid:
            arr+=x
        arr.sort()
        n = len(arr)
        return arr[n//2]
