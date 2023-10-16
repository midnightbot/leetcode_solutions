class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum([x for x in range(1,n+1) if x%m != 0]) - sum([x for x in range(1,n+1) if x%m == 0])
        
