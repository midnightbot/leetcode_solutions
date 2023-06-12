class Solution:
    def smallestString(self, s: str) -> str:
        ## do this operation between two a's
        indx = []

        for x in range(len(s)):
            if s[x]!='a':
                indx.append(x)
            if s[x] == 'a':
                if len(indx)!=0:
                    break
                else:
                    continue

        def format_ans(ip):
            res = ''
            for x in range(len(ip)):
                res+=chr(ord(ip[x]) - 1)

            return res

        if len(indx) == 0:
            return s[:-1] + 'z'
        elif len(indx) == 1:
            ans = s[:indx[0]] + format_ans(s[indx[0]]) + s[indx[0]+1:]
            return ans
        else:
            indx = [indx[0], indx[-1]]
        
            

            ans = s[:indx[0]] + format_ans(s[indx[0] : indx[1]+1]) + s[indx[1]+1:]

            return ans
                
        
