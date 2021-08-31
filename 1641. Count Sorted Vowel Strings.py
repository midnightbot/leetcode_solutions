class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        rows, cols = (n,5)
        arr = [[1]*cols]*rows
        #print(arr)
        
        for x in range(1,n):
            for y in range(5):
                if y == 0:
                    arr[x][y] = arr[x-1][0]+arr[x-1][1]+arr[x-1][2]+arr[x-1][3]+arr[x-1][4]
                elif y==1:
                    arr[x][y] = arr[x-1][1]+arr[x-1][2]+arr[x-1][3]+arr[x-1][4]
                elif y==2:
                    arr[x][y] = arr[x-1][2]+arr[x-1][3]+arr[x-1][4]
                elif y==3:
                    arr[x][y] = arr[x-1][3]+arr[x-1][4]
                else:
                    arr[x][y] =1
                
                
        return sum(arr[n-1])
 
