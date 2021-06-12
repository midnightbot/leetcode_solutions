class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        a=0
        b=0
        for x in range(0,int(len(s)/2)):
            if s[x]=="a" or s[x]=="e" or s[x]=="i" or s[x]=="o" or s[x]=="u" or s[x]=="A" or s[x]=="E" or s[x]=="I" or s[x]=="O" or s[x]=="U":
                a=a+1
                
            y = x + int(len(s)/2)
            if s[y]=="a" or s[y]=="e" or s[y]=="i" or s[y]=="o" or s[y]=="u" or s[y]=="A" or s[y]=="E" or s[y]=="I" or s[y]=="O" or s[y]=="U":
                b=b+1
                
        if a==b:
            return True
        else:
            return False
        
