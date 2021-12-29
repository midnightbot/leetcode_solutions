##ss
##solution 1 (Solving Recursively) (Time Limit Exceeded)
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
        ## allowed operations
        ## (x,y) -> (x,x+y)
        ## (x,y) -> (x+y,y)
        ans = []
        self.solve(sx,sy,tx,ty,ans)
        
        return len(ans)>=1
    def solve(self,x,y,finalx,finaly,ans):
        #print((x,y))
        if len(ans) < 1:
            
            if x == finalx and y == finaly:
                #print("inside")
                ans.append(1)
                
                
            elif x <= finalx and y <= finaly:
                
                self.solve(x+y,y,finalx,finaly,ans)
                self.solve(x,y+x,finalx,finaly,ans)
        
        
        
        
    
## Solution 2 (Accepted)
##rather than starting from sx,sy and going to tx,ty
##start from tx,ty and go to sx,sy

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
        ## allowed operations
        ## (x,y) -> (x,x+y)
        ## (x,y) -> (x+y,y)
        
        while tx>=sx and ty>=sy:
            
            if tx == sx and ty == sy: ## ans if found
                return True
            
            elif ty > tx and (ty-sy) // tx >=1: ## if ty > tx then tx=tx-ty operation cant be done as it will lead to -ve number and bound of input is from 1 to 10^9
                ##therefore try to subtract as many multiples of tx from ty
                ty-= ((ty-sy)//tx)*tx
                
            elif tx > ty and (tx-sx)//ty>=1: ## same as above
                tx-= ((tx-sx)//ty) * ty
                
            else:##if we are not able to subtract even 1 multiple of tx from ty or ty from tx, we are stuck at this point and hence no answer can be found
                return False
