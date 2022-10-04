##ss
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        
        asteroids = sorted(asteroids)
        
        ##mass >= asteroids[x] mass will become more
        ##else return false
        #print(asteroids)
        for x in range(len(asteroids)):
            if mass >= asteroids[x]:
                mass+=asteroids[x]
                
            else:
                return False
                
        return True
        
        
        
