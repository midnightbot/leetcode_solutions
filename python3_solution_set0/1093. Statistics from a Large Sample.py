class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        
        minimum = 0
        maximum = 0
        mean = 0
        median = 0
        mode = 0
        
        for x in range(len(count)): #minimum
            if count[x]!=0:
                minimum = float(x)
                break
                
        for y in range(len(count)-1,-1,-1): #maximum
            if count[y]!=0:
                maximum = float(y)
                break
                
        counts = 0
        sums = 0
        for x in range(len(count)): #mean
            if count[x]!=0:
                counts+= count[x]
                sums+= count[x]*x
                
        mean = sums / counts
        
        maxs = max(count)
        mode = count.index(maxs) #mode
        #print(mode)
        
        tempo = 0
    
        #print(counts)
        if counts%2==0: # median
            for x in range(len(count)):
                tempo+= count[x]
                if tempo == int(counts/2):
                    for z in range(x+1,len(count)):
                        if count[z]!=0:
                            median = float((x+z)/2)
                            break
                
                    break
                
                elif tempo > int(counts/2):
                    median = x
                    break
            
    
          
        elif counts%2!=0:
            for x in range(len(count)):
                tempo+= count[x]
                if tempo >= int(counts/2 + 1):
                    median = x
                    break
            

                
        
            
        
            
        print(counts)
        ans = []
        ans.append(minimum)
        ans.append(maximum)
        ans.append(mean)
        ans.append(median)
        ans.append(mode)
        
        return ans
        
        
