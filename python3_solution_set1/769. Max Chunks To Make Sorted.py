##ss
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        ## max chunks in any case <= len(arr)
        ## numbers inside chunk are sorted, not the chunk themselves
        ## [0,n-1] numbers
        
        chunk = 0
        seen = []
        prev = -1
        last_pos = -1
        
        for x in range(len(arr)):
            seen.append(arr[x])
            
            nochunk = False
            for y in range(1, x - last_pos + 1):
                #print(prev+y)
                if prev + y not in seen:
                    nochunk = True
                    break
            #print("--")
            if nochunk == False:
                chunk+=1
                prev = max(seen)
                seen = []
                last_pos = x
               
            #print(seen,prev,chunk,arr[x])
        #print(chunk,seen)
        return chunk if len(seen) == 0 else chunk + 1   
        
        
        
