class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        ## xx yy mismatch -> cost 1
        ## xy yx mismatch -> cost 2
        temp = Counter(s1+s2)
        for it in temp:
            if temp[it]%2!=0:
                return -1

        x1 = 0
        y1 = 0

        x2 = 0
        y2 = 0

        for x in range(len(s1)):
            if s1[x]!=s2[x]:
                if s1[x] == 'x':
                    x1+=1
                if s1[x] == 'y':
                    y1+=1

                if s2[x] == 'x':
                    x2+=1
                if s2[x] == 'y':
                    y2+=1

        
        ans = 0

        ## xx yy match
        pairs = min(x1//2, y2//2)
        ans+=pairs
        x1-=2*pairs
        y2-=2*pairs

        ## yy xx match
        pairs = min(y1//2, x2//2)
        ans+=pairs
        y1-=2*pairs
        x2-=2*pairs

        ## xy yx match
        pairs = (x1+y1)//2
        ans+=2*pairs
        
        return ans
