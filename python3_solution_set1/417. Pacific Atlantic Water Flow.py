##ss
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ##up,down,left,right water flow
        #ans = []
        ##simple that number should be max in (up or down) and (left or right)
        
        ##approach 2 : find pacific cover, find atlantic cover, find intersection
        pacific = [[0 for x in range(len(heights[0]))]for y in range(len(heights))]
        
        q = []
        
        for x in range(len(pacific)):
            pacific[x][0] = 1
            q.append([x,0])
        for x in range(len(pacific[0])):
            pacific[0][x] = 1
            q.append([0,x])

        a = self.cover_area(heights,pacific,q)
        
        atlantic = [[0 for x in range(len(heights[0]))]for y in range(len(heights))]
        q = []
        for x in range(len(atlantic)):
            q.append([x,len(atlantic[0])-1])
            atlantic[x][len(atlantic[0])-1] = 1
            
        for x in range(len(atlantic[0])):
            q.append([len(atlantic)-1,x])
            atlantic[len(atlantic)-1][x] = 1
            
        b = self.cover_area(heights,atlantic,q)
        return self.find_intersection(a,b)
    def cover_area(self,heights,pac,q):
        visited = set()
        while q:
            for x in range(len(q)):
                node = q.pop(0)
                visited.add(tuple([node[0],node[1]]))
                pac[node[0]][node[1]] = 1
                if node[0]-1>=0 and tuple([node[0]-1,node[1]]) not in visited and  heights[node[0]-1][node[1]] >= heights[node[0]][node[1]]:
                    q.append([node[0]-1,node[1]])
                    visited.add(tuple([node[0]-1,node[1]]))
                    
                if node[0] + 1 < len(heights) and tuple([node[0]+1,node[1]]) not in visited and heights[node[0]+1][node[1]] >= heights[node[0]][node[1]]:
                    q.append([node[0]+1,node[1]])
                    visited.add(tuple([node[0]+1,node[1]]))
                    
                    
                if node[1]-1>=0 and tuple([node[0],node[1]-1]) not in visited and heights[node[0]][node[1]-1]>= heights[node[0]][node[1]]:
                    q.append([node[0],node[1]-1])
                    visited.add(tuple([node[0],node[1]-1]))
                    
                    
                if node[1]+1 < len(heights[0]) and tuple([node[0],node[1]+1]) not in visited and heights[node[0]][node[1]+1] >= heights[node[0]][node[1]]:
                    q.append([node[0],node[1]+1])
                    visited.add(tuple([node[0],node[1]+1]))
                    
                
                    
                
        return pac
    
    def find_intersection(self,arr1,arr2):
        ans  = []
        for x in range(len(arr1)):
            for y in range(len(arr1[0])):
                if arr1[x][y] == arr2[x][y] == 1:
                    ans.append([x,y])
                    
        return ans
       
