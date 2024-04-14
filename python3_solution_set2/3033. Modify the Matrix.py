class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        max_cols = {x:-float('inf') for x in range(len(matrix[0]))}

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                max_cols[y] = max(max_cols[y], matrix[x][y])

        ans = copy.deepcopy(matrix)
        for x in range(len(ans)):
            for y in range(len(ans[0])):
                if ans[x][y] == -1:
                    ans[x][y] = max_cols[y]

        return ans

        
