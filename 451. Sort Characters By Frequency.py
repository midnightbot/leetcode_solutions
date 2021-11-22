##ss
class Solution:
    def frequencySort(self, s: str) -> str:
        
        print(s)
        strs=sorted(s)
        queue = []
        
        k = 1
        for x in range(1,len(strs)):
            if strs[x] == strs[x-1]:
                k+=1
                
            else:
                
                queue.append((k,strs[x-1]))
                k = 1
        queue.append((k,strs[x]))
        queue = sorted(queue,reverse = True)
        
        ans  = ""
        while queue:
            elem = queue.pop(0)
            
            for x in range(elem[0]):
                ans+=elem[1]
                
        return ans
