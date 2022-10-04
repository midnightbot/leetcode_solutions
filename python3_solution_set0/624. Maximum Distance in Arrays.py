##ss
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        
        compare = []
        
        for x in range(len(arrays)):
            compare.append((arrays[x][0],x))
            compare.append((arrays[x][len(arrays[x])-1],x))
            
        compare = sorted(compare,key = lambda x:x[0])
        #print(compare)
        done = False
        i = 0
        j = len(compare) - 1
        
        while not done:
            if compare[i][1]!=compare[j][1]:
                ans = abs(compare[i][0]-compare[j][0])
                done = True
                
            elif compare[i][1] == compare[j][1]:
                if abs(compare[i+1][0] - compare[j][0]) > abs(compare[i][0] - compare[j-1][0]):
                    i+=1
                    
                else:
                    j-=1
                
        return ans
            
                
       
        
