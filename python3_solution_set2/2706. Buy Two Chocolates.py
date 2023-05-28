class Solution:
    def buyChoco(self, p: List[int], money: int) -> int:
        
        p.sort()
        if p[0] + p[1] <= money:
            return money - p[0] -p[1]
        else:
            return money
        
