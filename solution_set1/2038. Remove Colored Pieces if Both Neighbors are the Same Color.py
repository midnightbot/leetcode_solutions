##ss
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        acount = 0
        bcount = 0
        
        prev = colors[0]
        count = 1
        for x in range(1,len(colors)):
            if colors[x] == prev:
                count+=1
                
            else:
                if prev == 'A':
                    if count>=3:
                        acount+=count - 2
                        
                    prev = colors[x]
                    count = 1
                    
                    
                elif prev == "B":
                    if count >=3:
                        bcount+=count - 2
                        
                    prev = colors[x]
                    count = 1
                    
        if prev == 'A':
            if count>=3:
                acount+=count - 2
                
                
        elif prev == "B":
            if count>=3:
                bcount+=count - 2
                
        return acount > bcount
        
