##ss
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        ans = []
        ans.append(0)
        prev_index = len(heights) - 1
        prev_max = heights[len(heights)-1]
        for x in range(len(heights)-2,-1,-1):
            #print(ans)
            if heights[x] <= heights[x+1]:
                prev_index = x
                prev_max = heights[x]
                ans.append(1)
                
            elif heights[x] > heights[x+1]:
                #print("inside",x,prev_index,prev_max)
                temp = 1
                #print(temp)
                for y in range(prev_index, len(heights)):
                    if heights[x] > prev_max and heights[y] > prev_max:
                        temp+=1
                        prev_index = y-1
                        prev_max = min(heights[x],heights[y])
                        
                    elif heights[y] > heights[x]:
                        break
                        
                    
                   
                        #temp+=1
                        #prev_max = heights[y]
                        #prev_index = y
                        
                    
                        
                ans.append(temp)
        return ans[::-1]
                        
                    
               
        
