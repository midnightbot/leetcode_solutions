##ss
##Naive Solution 1

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans  = [[0 for x in range(26)] for y in range(len(strs))]
        
        print(ord('a'))
        for x in range(len(strs)):
            for y in range(len(strs[x])):
                ans[x][ord(strs[x][y]) -97]+=1
                
        final_ans = []
        visited = []
        for x in range(len(strs)):
            if x not in visited:
                temp = []
                visited.append(x)
                temp.append(strs[x])
                for y in range(x+1,len(strs)):
                    if ans[x] == ans[y]:
                        visited.append(y)
                        temp.append(strs[y])
                        
                final_ans.append(temp)
                
        return final_ans
                        
        
