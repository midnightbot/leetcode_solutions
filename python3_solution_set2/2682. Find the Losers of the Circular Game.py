class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        not_seen = [-1 for x in range(n)]

        done = False
        turn = 1
        curr = 0
        not_seen[0] = 0
        while not done:
            next = (curr + turn*k)%n
            if not_seen[next] == -1:
                not_seen[next] = 0
                turn+=1
                curr = next
            else:
                done = True
        ans = []

        for indx, x in enumerate(not_seen):
            if x==-1:
                ans.append(indx+1)

        return ans
