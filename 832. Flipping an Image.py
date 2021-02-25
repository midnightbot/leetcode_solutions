class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for x in range(len(image)):
            image[x] = list(reversed(image[x]))
            for y in range(len(image[0])):
                if image[x][y]==0:
                    image[x][y]=1
                else:
                    image[x][y]=0
                    
        return image
        
        
            
        
