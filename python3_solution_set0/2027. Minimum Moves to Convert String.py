class Solution:
    def minimumMoves(self, s: str) -> int:
        
        moves = 0
        x=0
        while x<=len(s)-1:
            #print(x)
            if s[x] == 'X':
               # print("inside")
                moves+=1
                x = x+2
                
            
            x=x+1
                
        return moves
            
        
