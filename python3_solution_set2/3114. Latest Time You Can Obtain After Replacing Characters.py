class Solution:
    def findLatestTime(self, s: str) -> str:
        s = [x for x in s]
        if s[0] == '?':
            if s[1]!='?' and int(s[1]) >= 2:
                s[0] = '0'
            else:
                s[0] = '1'

        if s[1] == '?':
            if s[0] == '1':
                s[1] = '1'
            else:
                s[1] = '9'

        if s[3] == '?':
            s[3] = '5'
        if s[4] == '?':
            s[4] = '9'
        return "".join(s)
        
