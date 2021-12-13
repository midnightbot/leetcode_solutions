##ss
##Solution 1
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        x = 0
        y = 0
        
        for m in range(len(moves)):
            if moves[m] == "U":
                y+=1
                
            elif moves[m] == "D":
                y-=1
                
            elif moves[m] == "R":
                x+=1
                
            else:
                x-=1
                
        if x==0 and y==0:
            return True
        
        else:
            return False
        
 ##Solution 2
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        u = 0
        d = 0
        r = 0
        l = 0
        
        for x in range(len(moves)):
            if moves[x] == "U":
                u+=1
                
            elif moves[x] == "D":
                d+=1
                
            elif moves[x] == "R":
                r+=1
                
            else:
                l+=1
                
        if r==l and u==d:
            return True
        else:
            return False
        
