class Solution:
    def find_ans(self, s):
        ans = ""

        for x in range(len(s)-1):
            a = int(s[x])
            b = int(s[x+1])
            ans+=str((a+b)%10)
        return ans
    def hasSameDigits(self, s: str) -> bool:

        while len(s)!=2:
            s = self.find_ans(s)
        
        return len(set(s)) == 1


        
