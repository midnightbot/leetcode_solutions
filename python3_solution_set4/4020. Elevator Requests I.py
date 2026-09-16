class Solution:
    def elevatorRequests(self, n: int, req: list[int]) -> int:
        ans = 0
        req = [0] + req
        for x in range(len(req)-1):
            ans+=abs(req[x+1] - req[x])
        return ans
        
