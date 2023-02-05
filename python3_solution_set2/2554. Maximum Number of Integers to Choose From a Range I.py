class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        seen = set(banned)
        curr = 0
        count = 0
        for x in range(1,n+1):
            diff = maxSum - curr
            if x > diff:
                break

            elif x not in seen:
                curr+=x
                count+=1

        return count

            
