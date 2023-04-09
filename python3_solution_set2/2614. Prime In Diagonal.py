import math
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:

        def prime_check(n):
            if n == 1:
                return False
            for x in range(2, int(math.sqrt(n))+1):
                if n%x == 0:
                    return False

            return True

        
        arr = []
        n = len(nums)
        for x in range(n):
            arr.append(nums[x][x])

        
        for x in range(n-1,-1,-1):
            arr.append(nums[n-x-1][x])

        arr.sort(reverse = True)
        
        for it in arr:
            if prime_check(it):
                return it

        return 0
