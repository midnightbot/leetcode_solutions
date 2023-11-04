class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:

        ## when ants meet, they change direction and continue moving
        ## so we can consider they continue moving in same direction
        ## hence ans would be max time of any ant to fall


        ans = 0

        for i in right:
            ans = max(ans, n - i)

        for i in left:
            ans = max(ans, i)

        return ans
        
