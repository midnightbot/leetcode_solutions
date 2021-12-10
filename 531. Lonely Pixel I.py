##ss
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        
        lonely = 0
        
        for x in range(len(picture)):
            for y in range(len(picture[0])):
                if picture[x][y] == "B":
                    r = 0
                    c = 0
                    for z in range(len(picture[0])):
                        if (picture[x][z] == "B" or picture[x][z] == -1) and z!=y:
                            picture[x][z] = -1
                            r+=1
                            
                    
                       
                    for k in range(len(picture)):
                        if (picture[k][y] == "B" or picture[k][y] == -1) and k!=x:
                            c+=1
                            picture[k][y] = -1
                        
                    if r>0 or c>0:
                        picture[x][y] = -1
                        
                    else:
                        lonely +=1
                    
                
                        
        return lonely
        
