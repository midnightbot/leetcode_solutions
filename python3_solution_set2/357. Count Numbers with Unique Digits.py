import math
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans = 0
        if n == 0:
            return 1
        elif n == 1:
            return 10

        arr = [9,9] + [8-x for x in range(9)]
        
        for x in range(n+1):
            temp = 1
            for y in range(x):
                temp*=arr[y]

            ans+=temp
        return ans
