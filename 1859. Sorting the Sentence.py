
class Solution:
    def sortSentence(self, s: str) -> str:
        
        temp = s.split()
        ans = []
        str_ans = ""
        for x in range(len(temp)):
            ans.append((temp[x][len(temp[x])-1],temp[x][0:len(temp[x])-1]))
            
        ans = sorted(ans)
        print(ans)
        for x in range(len(ans)):
            str_ans += str(ans[x][1]) + " "
            
        return str_ans[0:len(str_ans)-1]
            
        
        
