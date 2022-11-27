class Solution:
    def pivotInteger(self, n: int) -> int:

        for x in range(1,n+1):
            if sum([i for i in range(1,x+1)]) == sum([i for i in range(x,n+1)]):
                return x

        return -1
