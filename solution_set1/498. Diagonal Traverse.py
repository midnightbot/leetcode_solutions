##ss
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        thisans = []
        result = []
        c = 0 
        ##first column
        for x in range(len(mat)):
            a = x
            b = 0
            thisans = []
            while a>=0 and b < len(mat[0]):
                thisans.append(mat[a][b])
                a-=1
                b+=1
                
            if c%2!=0:
                thisans = thisans[::-1]
                
            result+=thisans
            c+=1
        print(result)
        
        ##last row
        for x in range(1,len(mat[0])):
            a = len(mat)-1
            b = x
            thisans = []
            while a>=0 and b < len(mat[0]):
                thisans.append(mat[a][b])
                a-=1
                b+=1
                
            if c%2!=0:
                thisans = thisans[::-1]
                
            result+=thisans
            c+=1
            
        return result
                
        
        
