##ss
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        children = {x:[] for x in range(len(s))}
        maxs = [0]
        
        for indx,val in enumerate(parent):
            if val >=0:
                children[val].append(indx)
             
        def dfs(root):

            temp = [0]
            for nei in children[root]:
                save = dfs(nei)
                if s[nei] != s[root]:
                    temp.append(save)

            temp = nlargest(2, temp)
            maxs[0] = max(maxs[0], 1 + sum(temp))
            #print(temp)
            return max(temp)+1
            
        dfs(0)
        return maxs[0]
