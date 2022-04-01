##ss
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ## same as 769. Max Chunks To Make Sorted

        ## instead numbers being in range [0,n-1] they can be anything
        ## also repeated numbers, hence store freq count of each number
        comp_arr = copy.deepcopy(arr)
        comp_arr = sorted(comp_arr)
        
        #print(comp_arr)
        
        chunk = 0
        seen = {}
        prev = comp_arr[0]
        last_pos = -1
        
        for x in range(len(arr)):
            #seen.append(arr[x])
            seen[arr[x]] = seen.get(arr[x],0) + 1
            
            nochunk = False
            seencopy = copy.deepcopy(seen)
            for y in range(last_pos + 1 ,x+1):
                #print(prev+y)
                if comp_arr[y] not in seencopy:
                    nochunk = True
                    break
                else:
                    seencopy[comp_arr[y]]-=1
                    
                    if seencopy[comp_arr[y]] == 0:
                        seencopy.pop(comp_arr[y])
            #print("--")
            if nochunk == False:
                chunk+=1
                prev = max(seen)
                seen =  {}
                last_pos = x
               
            #print(seen,prev,chunk,arr[x])
        #print(chunk,seen)
        return chunk if len(seen) == 0 else chunk + 1
        
