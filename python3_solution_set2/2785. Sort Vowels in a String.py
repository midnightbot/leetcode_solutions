class Solution:
    def sortVowels(self, s: str) -> str:
        ans = []
        temp = []
        for i in s:
            if i not in 'aeiouAEIOU':
                ans.append(i)
            else:
                ans.append('?')
                temp.append(i)

        temp = [(x,ord(x)) for x in temp]
        temp = sorted(temp, key = lambda x:x[1])
        temp = [x[0] for x in temp]
        i = 0
        
        for x in range(len(ans)):
            if ans[x] == "?":
                ans[x] = temp[i]
                i+=1

        return "".join(ans)
