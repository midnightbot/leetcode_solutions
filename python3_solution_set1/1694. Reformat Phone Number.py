##ss
class Solution:
    def reformatNumber(self, number: str) -> str:
        
        s = ""
        
        for x in range(len(number)):
            if ord(number[x])>=ord('0') and ord(number[x])<=ord('9'):
                s+=number[x]
                
        #print(s)
        lens = len(s)
        ans = []
        p = 0
        while lens > 4:
            
            ans.append(s[p:p+3])
            p+=3
            lens-=3
            
        if lens < 4:
            ans.append(s[p:])
            
        else:
            ans.append(s[p:p+2])
            p+=2
            ans.append(s[p:])
            
        return '-'.join(ans)
