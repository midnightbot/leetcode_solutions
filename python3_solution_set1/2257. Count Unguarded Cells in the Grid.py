##ss
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        arr = [[0 for x in range(n)] for y in range(m)]
        
        for x,y in walls:
            arr[x][y] = -1
            
        #print(arr)
        for x,y in guards:
            arr[x][y] = 2
            
        def expand(posx,posy):
            
            ##right side
            ycor = posy + 1
            while ycor < len(arr[0]):
                if arr[posx][ycor] in [-1,2]:
                    break
                    
                else:
                    arr[posx][ycor] = 1
                ycor+=1
                
            ##left side
            ycor = posy - 1
            while ycor >= 0:
                if arr[posx][ycor] in [-1,2]:
                    break
                else:
                    arr[posx][ycor] = 1
                    
                ycor-=1
                
            ##up
            xcor = posx - 1
            
            while xcor >=0:
                if arr[xcor][posy] in [-1,2]:
                    break
                else:
                    arr[xcor][posy] = 1
                    
                xcor-=1
                
            ##down
            
            xcor = posx + 1
            while xcor < len(arr):
                if arr[xcor][posy] in [-1,2]:
                    break
                    
                else:
                    arr[xcor][posy] = 1
                    
                xcor+=1
                
        for x,y in guards:
            expand(x,y)
            #arr[x][y] = 2
            
        #print(arr)
        result = 0
        for x in range(len(arr)):
            result+= arr[x].count(0)
            
            
        return result
        
