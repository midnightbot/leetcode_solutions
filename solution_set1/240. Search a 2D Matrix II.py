##ss
##simple divide and conquer
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        visited = set()
        ans = []
        if matrix == None:
            return False
        if len(matrix) <=3 or len(matrix[0]) <=3:
            for x in range(len(matrix)):
                for y in range(len(matrix[0])):
                    if matrix[x][y] == target:
                        return True
                    
            return False
            
        def divide(startrow,endrow,startcol,endcol):
            print(startrow,endrow,startcol,endcol)
            midrow = startrow + (endrow-startrow)//2
            midcol = startcol + (endcol-startcol)//2
            
            if startrow == endrow and startcol == endcol and matrix[startrow][startcol] == target:
                print("inside")
                #ans = True
                #print(ans)
                ans.append(1)
                return startrow,endrow
            
            
            elif startrow >=0 and endrow<len(matrix) and startcol>=0 and endcol < len(matrix[0]) and (startrow!=endrow or startcol!=endcol) and len(ans)==0:
                #print("hi")
                if matrix[startrow][startcol] <=target <=matrix[midrow][midcol] and tuple((startrow,midrow,startcol,midcol)) not in visited:
                    visited.add(tuple((startrow,midrow,startcol,midcol)))
                    divide(startrow,midrow,startcol,midcol)
                    
                if midcol+1 < len(matrix[0]) and matrix[startrow][midcol+1] <=target <=matrix[midrow][endcol] and tuple((startrow,midrow,midcol+1,endcol)) not in visited:
                    visited.add(tuple((startrow,midrow,midcol+1,endcol)))
                    divide(startrow,midrow,midcol+1,endcol)
                #print(midrow)   
                if midrow+1 < len(matrix) and matrix[midrow+1][startcol] <=target<=matrix[endrow][midcol] and tuple((midrow+1,endrow,startcol,midcol)) not in visited:
                    visited.add(tuple((midrow+1,endrow,startcol,midcol)))
                    divide(midrow+1,endrow,startcol,midcol)
                if midrow+1 < len(matrix) and midcol+1 < len(matrix[0]) and matrix[midrow+1][midcol+1]<=target<=matrix[endrow][endcol] and tuple((midrow+1,endrow,midcol+1,endcol)) not in visited:
                    visited.add(tuple((midrow+1,endrow,midcol+1,endcol)))
                    divide(midrow+1,endrow,midcol+1,endcol)
                
                
                
        ans = []
        divide(0,len(matrix)-1,0,len(matrix[0])-1)
        return len(ans) >=1
            
        
