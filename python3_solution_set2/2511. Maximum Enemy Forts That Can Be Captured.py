class Solution:
    def captureForts(self, forts: List[int]) -> int:

        ## -1, 0 , 1
        ## no, enemy, my

        j = 0
        ans = 0
        for i in range(len(forts)):
            if forts[i] != 0:
                if forts[j] == -forts[i]:
                    ans = max(ans, i-j-1)
                j = i
        return ans


