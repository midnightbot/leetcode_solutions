class Solution:
    def minimumLength(self, s: str) -> int:
        temp = dict(Counter(s))
        delete = 0
        for x in temp:
            delete += max(0, (temp[x]-1)//2)
        return len(s) - 2*delete
        
