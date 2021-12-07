##ss gg
##
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        
        
        counter = len(asteroids) - 1
        prev_len = len(asteroids)
        c = 0
        ok = 0
        while counter > 0:
            #print(counter)
            #print(asteroids)
            if asteroids[counter] < 0:
                #print("hello")
                c = 0
                for x in range(counter-1,-1,-1):
                    
                    if asteroids[x] >= -1 * asteroids[counter]:
                        c = 2
                        break
                    elif asteroids[x] < 0:
                        c = 1
                        break
                    
                        
                if c == 1 and x!=counter-1:
                    #print("he")
                    asteroids = asteroids[0:x+1] + asteroids[counter:len(asteroids)]
                elif c== 2:
                    #print("inside")
                    if x == 0 and asteroids[0] < -1 * asteroids[counter] and asteroids[0] > 0:

                        asteroids = asteroids[counter:len(asteroids)]

                    elif x == 0 and asteroids[0] > -1 * asteroids[counter]:

                        asteroids = asteroids[0:1] + asteroids[counter+1:len(asteroids)]

                    elif x == 0 and asteroids[0] == -1 * asteroids[counter]:
                        asteroids = asteroids[counter+1:len(asteroids)]
                    elif x!=0 and asteroids[x] == -1 * asteroids[counter]:
                        asteroids = asteroids[0:x] + asteroids[counter+1:len(asteroids)]

                    elif x!=0 and asteroids[x] > -1 * asteroids[counter]:
                        asteroids = asteroids[0:x+1] + asteroids[counter+1 : len(asteroids)]
                        
                elif c == 0:
                    asteroids = asteroids[counter:len(asteroids)]
                   
            if prev_len == len(asteroids):
                counter-=1
                
                
            else:
                counter = len(asteroids) - 1
                prev_len = len(asteroids)
            #print(asteroids)
            
        return asteroids
            
        
