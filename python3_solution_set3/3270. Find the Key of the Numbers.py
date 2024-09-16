class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:

        def conv(s):
            s = str(s)
            for x in range(4-len(s)):
                s = '0'+s
            return s
        
        num1 = conv(num1)
        num2 = conv(num2)
        num3 = conv(num3)
        ans = ''
        for x in range(4):
            ans+=str(min(int(num1[x]), int(num2[x]), int(num3[x])))
        return int(ans)
