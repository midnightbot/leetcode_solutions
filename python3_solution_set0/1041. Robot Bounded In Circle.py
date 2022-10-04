##ss
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        ##0 -> north       1->east             2->south                   3-> west 
        loc = [0,0]
        face = 0
        
        for x in range(len(instructions)):
            #print(loc)
            if instructions[x] == "G":
                if face == 0:
                    loc[1]+=1
                    
                elif face == 1:
                    loc[0]+=1
                    
                elif face == 2:
                    loc[1]-=1
                    
                else:
                    loc[0]-=1
                    
            elif instructions[x] == "L":
                #print("hi")
                face = (face - 1)%(4)
                
                
            elif instructions[x] == "R":
                face = (face + 1)%(4)
        
        #print(loc,face)
        if loc == [0,0] or face!=0:
            return True
        
        
        else:
            return False
                
        
