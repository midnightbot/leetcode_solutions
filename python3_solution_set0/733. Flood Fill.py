class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        
        queue = set()
        queue.add(tuple((sr,sc)))
        vals = image[sr][sc]
        if vals == newColor:
            return image
        
        while queue:
            #print(queue)
            node = queue.pop()
            #print("hi",node)
            image[node[0]][node[1]] = newColor
            #print(image)
            if node[0]+1<len(image):
                if image[node[0]+1][node[1]]==vals:
                    queue.add(tuple((node[0]+1,node[1])))
                    
            if node[0]-1>=0:
                if image[node[0]-1][node[1]]==vals:
                    queue.add(tuple((node[0]-1,node[1])))
                    
            if node[1]+1<len(image[0]):
                if image[node[0]][node[1]+1]==vals:
                    queue.add(tuple((node[0],node[1]+1)))
                    
            if node[1]-1>=0:
                if image[node[0]][node[1]-1]==vals:
                    queue.add(tuple((node[0],node[1]-1)))
                    
                    
        return image
                
                
        
