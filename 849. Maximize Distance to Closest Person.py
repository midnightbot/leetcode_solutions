##ss
import math
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        ##max number of continuous zeros between any two ones would be the place where alex will sit. Alex will sit in middle of such a space to maximize the dist
        
        ##if seats from start are empty, special consition, only need to check max dist on right side. Similar is the case when ending seats are empty
        ans = 0
        
        zeros = 0
        final_ans = 0
        end = True
        for x in range(len(seats)):
            #print(zeros)
            if seats[x] == 1:
                ans = max(ans,zeros)
                if end == True:
                    final_ans = zeros
                    end = False
                else:
                    final_ans = max(final_ans,math.ceil(ans/2)) 
                    
                zeros = 0
                
            else:
                zeros+=1
            #print(zeros)
            
        final_ans = max(final_ans,zeros)
        #ans = max(ans,zeros)        
        return final_ans
        
