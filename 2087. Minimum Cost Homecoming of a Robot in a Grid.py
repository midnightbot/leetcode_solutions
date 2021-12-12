##ss
## simple greedy one solution problem
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        
        
        ##cover all rows and all columns
        ##very direct question
        
        cost = 0
        
        if homePos[0] > startPos[0]:
            
            temp = homePos[0] - startPos[0]
            for x in range(temp):
                cost+=rowCosts[startPos[0]+1+x]
                
            #print(cost)
            
            if homePos[1] > startPos[1]: 
                ##home is to right
                temp = homePos[1] - startPos[1]
                for x in range(temp):
                    cost+=colCosts[startPos[1]+x+1]
              
            else:
                ##home to left or no same pos
                temp = startPos[1] - homePos[1]
                for x in range(temp):
                    cost+=colCosts[startPos[1]-1-x]
                    
                    
        else:
            temp = startPos[0] - homePos[0]
            for x in range(temp):
                cost+=rowCosts[startPos[0]-1-x]
                
                
            if homePos[1] > startPos[1]: 
                ##home is to right
                temp = homePos[1] - startPos[1]
                for x in range(temp):
                    cost+=colCosts[startPos[1]+x+1]
              
            else:
                ##home to left or no same pos
                temp = startPos[1] - homePos[1]
                for x in range(temp):
                    cost+=colCosts[startPos[1]-1-x]
                
                
            
        return cost
        
        
        
