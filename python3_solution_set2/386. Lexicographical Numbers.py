class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [x for x in range(1,n+1)]

        ans = [str(x) for x in ans]

        ans = sorted(ans, key = lambda x:len(x))
        ans = sorted(ans)
        
        return [int(x) for x in ans]
