##ss
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ##keep on storing the boundaries of matrix and shrinking size
        ##startrow+=1 endrow-=1 startcol+=1 endcol-=1
        startrow = 0
        endrow = len(matrix)
        startcol = 0
        endcol = len(matrix[0])
        result = []
        while startrow < endrow and startcol < endcol:
            #print(startrow,endrow,startcol,endcol)
            ##1st row
            for x in range(startcol,endcol):
                result.append(matrix[startrow][x])
                
            
            
            
            ##last col
            for x in range(startrow+1,endrow):
                result.append(matrix[x][endcol-1])
                
            
            
            ##last row
            if endrow-startrow > 1:
                for x in range(endcol-2,startcol-1,-1):
                    result.append(matrix[endrow-1][x])
                
            
            
            ##first column
            if endcol - startcol > 1:
                for x in range(endrow-2,startrow,-1):
                    result.append(matrix[x][startcol])
                
            #print(result)
            
            
            startrow+=1
            endrow-=1
            startcol+=1
            endcol-=1
            
        return result
        
