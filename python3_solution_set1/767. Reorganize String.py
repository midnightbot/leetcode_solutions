##ss
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        ##idea : is to add as many characters to the answer every time that have same highest frequency and then reduce their frequency by 1
        ## if no other character has freq = highest freq : then just pick 2 characters with largest freq and 1 occurence of both in answer and append them back in the heap
        
        ##simply means there are 2 cases
        ##case1: many chrs have freq same as the highest freq, then add 1 occurence of each of them in result and append freq-1 of each chr back in heap
        ##case2: No other chr has freq same has highest freq, then select top 2 chr according to freq, add 1 occurence of both in the answer, append freq-1 for both chrs back in the heap
        dicts = {}
        comp = []
        for x in range(len(s)):
            if s[x] in dicts:
                dicts[s[x]]+=1
                
            else:
                dicts[s[x]] = 1
                
        for x in dicts:
            if dicts[x]!=0:
                heapq.heappush(comp,[-1*dicts[x],x])
        ans = ""
        
        while len(comp) > 1:
            head = heapq.heappop(comp)
            root = head[0]
            elem = [head]
            
            while comp and  root == head[0]:
                
                
                newr = heapq.heappop(comp)
                
                if len(elem) == 1:
                    elem.append(newr)
                    #root = newr[0]
                    
                elif len(elem) > 1:
                    if newr[0] == root:
                        elem.append(newr)
                    else:
                        heapq.heappush(comp,newr)
                        break
                        
                        
            for x in range(len(elem)):
                ans+=elem[x][1]
                elem[x][0]+=1
                
            for x in range(len(elem)):
                if elem[x][0]!=0:
                    heapq.heappush(comp,elem[x])
        
        if len(comp) == 0:
            return ans
        #print(comp,ans)
        if len(comp) == 1 and comp[0][0] == -1:
            if ans[-1]!=comp[0][1]:
                #print("insid")
                return ans + comp[0][1]
            
        return ""
        
