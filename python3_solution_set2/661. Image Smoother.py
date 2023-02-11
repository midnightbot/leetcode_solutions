import math
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        ans = [[0 for x in range(len(img[0]))] for y in range(len(img))]

        m = len(img[0])
        n = len(img)

        def find_ans(x,y):
            directions = ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1))

            sums = 0
            cnt = 0

            for r,c in directions:
                if 0<=r+x<n and 0<=c+y<m:
                    sums+=img[r+x][c+y]
                    cnt+=1

            
            return math.floor(sums/cnt) if cnt!=0 else 0


        for x in range(len(img)):
            for y in range(len(img[0])):
                ans[x][y] = find_ans(x,y)

        return ans
