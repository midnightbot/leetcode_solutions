class Solution:
    def largestVariance(self, s: str) -> int:

        ans = 0
        n = len(s)
        temp = list(set(s))
        ## always try to make 1st char +ve
        for x in temp:
            for y in temp:
                if x!=y:
                    cnt = 0
                    hasb = 0
                    firstb = 0

                    for it in range(n):
                        if s[it] == x:
                            cnt+=1

                        elif s[it] == y:
                            hasb = True
                            if firstb and cnt >=0:
                                firstb = False
                            
                            elif cnt-1 < 0:
                                firstb = True
                                cnt = -1

                            elif cnt-1>=0:
                                cnt-=1

                        if hasb:
                            ans = max(ans, cnt)

                        
        return ans
        
