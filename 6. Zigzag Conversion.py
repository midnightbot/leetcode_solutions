##ss
## simple, do as directed
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        ans = [[-1 for x in range(len(s))] for y in range(numRows)]
        x = 0
        y = 0
        
        counter = 0
        
        for z in range(len(s)):
           
            
            if counter>1:
                #print(counter)
                ans[x][y] = s[z]
                counter-=1
                x-=1
                y+=1
            elif counter == 1:
                ans[x][y] = s[z]
                counter = 0
                x+=1
            elif x == 0:
                ans[x][y] = s[z]
                x+=1
                
            elif x < numRows - 1:
                
                ans[x][y] = s[z]
                x+=1
                
            elif x == numRows - 1:
                
                counter = numRows - 1
                ans[x][y] = s[z]
                y+=1
                x-=1
        #print(ans)       
        for x in range(len(ans[0])-1,-1,-1):
            if ans[0][x]!=-1:
                indx = x
                break
                
        finals = ""
        for x in range(len(ans)):
            for y in range(len(ans[0])):
                if ans[x][y]!=-1:
                    finals+=ans[x][y]
                    
        return finals
