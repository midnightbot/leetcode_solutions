class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = 0
        maxs = 0

        for indx, r in enumerate(mat):
            c = r.count(1)
            if maxs < c:
                maxs = c
                ans = indx


        return [ans, maxs]
