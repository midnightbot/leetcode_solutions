##ss
class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        n = str(n)
        this = ""
        ans = []
        for x in range(len(n)-1,-1,-1):
            if len(this) < 3:
                this+=n[x]
                
            elif len(this) == 3:
                ans.append(this[::-1])
                this = ""
                this+=n[x]
                
        ans.append(this[::-1])
        
        ans = ans[::-1]
        return ".".join(ans)
        
