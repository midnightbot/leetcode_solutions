##ss
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        
        ans  = []
        
        pos = copy.copy(startPos)
        for x in range(len(s)):
            pos = copy.copy(startPos)
            stated = False
            for y in range(x,len(s)):
                #print(x,y,pos)
                anss = self.move(pos,s[y],n)
                if anss[0] == False:
                    stated = True
                    ans.append(y-x)
                    break
                pos = anss[1]
            if stated == False:
                ans.append(y-x+1)
                
        return ans
                
              
        
        
    def move(self,pos,operation,n):
        #print(pos,operation)
        if operation == "R":
            pos = [pos[0],pos[1]+1]
            
        elif operation == "L":
            pos = [pos[0],pos[1]-1]
            
        elif operation == "U":
            pos = [pos[0]-1,pos[1]]
            
        else:
            pos = [pos[0]+1,pos[1]]
            
        temp = self.check(pos,n)
        
        return temp,pos

        
    def check(self,pos,n):
        
        if pos[0] <0 or pos[0] >=n or pos[1] < 0 or pos[1] >=n:
            return False
        
        return True
        
