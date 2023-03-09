class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:

        ## (x, y-x)
        ## (x-y, y)
        ## (2*x, y)
        ## (x, 2*y)
        @cache
        def is_power_of_two(n):
            if n in [1,2]:
                return True
            elif n%2!=0:
                return False
            else:
                return is_power_of_two(n//2)

        ans = math.gcd(targetX, targetY)

        return is_power_of_two(ans)
