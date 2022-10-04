##ss
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        ##bulls -> digits that are in correct position
        ##cows -> correct digits but positon mentioned wrong
        
        ##x bulls y cows
        
        
        a = 0
        index = []
        b = 0
        sec = [secret[x] for x in range(len(secret))]
        gue = [guess[x] for x in range(len(guess))]
        for x in range(len(secret)):
            if secret[x] == guess[x]:
                a+=1
                index.append(x)
                sec[x] = "-"
                gue[x] = "-"
                
        print(sec,gue)
        
        for x in range(len(gue)):
            if gue[x]!="-":
                if gue[x] in sec:
                    b+=1
                    index = sec.index(gue[x])
                    gue[x] = "-"
                    sec[index] = "-"
                    
                
                    
                    
        ans = ""
        ans+=str(a)+"A"+str(b)+"B"
        return ans
                
       
