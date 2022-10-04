##Ss
##sort according to multiple keys
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        ans = []
        
        for x in range(len(arr)):
            ans.append((format(arr[x],"b").count("1"),arr[x]))
            
        ans = sorted(ans, reverse = True, key = lambda x:(x[0],x[1]))
        #ans = sorted(ans, key = lambda x:x[1])
        finals = []
        
        for x in range(len(ans)):
            finals.append(ans[x][1])
            
        return finals[::-1]
        
