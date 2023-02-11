class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:

        rounds = [x-1 for x in rounds]

        ans = [0 for x in range(n)]
        

        def upd_ans(start,end, it):
            if it!=0:
                start+=1
                start%=n

            while start!=end:
                ans[start]+=1
                start+=1
                start%=n

            ans[start]+=1

        for x in range(len(rounds)-1):
            upd_ans(rounds[x], rounds[x+1],x)
            #print(ans)

        maxs = max(ans)

        anss = []

        for x in range(len(ans)):
            if ans[x] == maxs:
                anss.append(x+1)

        return anss
