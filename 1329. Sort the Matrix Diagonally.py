##ss
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        dicts = {}
        
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                
                if x-y in dicts.keys():
                    dicts[x-y].append(mat[x][y])
                    
                else:
                    dicts[x-y] = [mat[x][y]]
                    
        dictspos = {}           
        
        for x in dicts.keys():
            dicts[x] = sorted(dicts[x])
            dictspos[x] = 0
            
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                mat[x][y] = dicts[x-y][dictspos[x-y]]
                dictspos[x-y]+=1
                
        return mat
                
         
                
        
