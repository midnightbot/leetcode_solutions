class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        
        s = [str(i) for i in A]
        res = int("".join(s))
        temp = res+K
        ans = [int(x) for x in str(temp)]
        return ans
        
