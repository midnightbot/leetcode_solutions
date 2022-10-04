##ss
import numpy as np
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        for x in range(len(box)):
            for y in range(len(box[0])-1,-1,-1):
                
                if box[x][y] == '#':
                    
                    cord1 = x
                    cord2 = y+1
                    
                    while cord2 < len(box[0]) and box[x][cord2] == '.':
                        cord2 +=1
                        
                    box[x][cord2-1] = "#"
                    
                    if cord2-1!=y:
                        box[x][y] = '.'
                        
        #print(box)
        newbox = np.array(box)
        newbox = newbox[::-1]
        newbox = newbox.T
        
        return newbox.tolist()
        
