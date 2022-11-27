class Solution:
    def numberOfCuts(self, n: int) -> int:
        return n//2 if n%2==0 else 0 if n==1 else n
