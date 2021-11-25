class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        full = capacity
        counter = 0
        steps = 0
        while counter < len(plants):
            if capacity >= plants[counter]:
                capacity-=plants[counter]
                steps+=1
                counter+=1
                
            else:
                capacity = full - plants[counter]
                steps+= 2*(counter) + 1
                counter+=1
                
        return steps
        
