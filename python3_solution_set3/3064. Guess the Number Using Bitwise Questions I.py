# Definition of commonSetBits API.
# def commonSetBits(num: int) -> int:

class Solution:
    def findNumber(self) -> int:

        ans = [0 for x in range(32)]
        for x in range(32):
            temp = commonSetBits(2**x)
            ans[x] = temp

        res = 0
        for x in range(len(ans)):
            if ans[x] == 1:
                res+=2**x
        return res
        
