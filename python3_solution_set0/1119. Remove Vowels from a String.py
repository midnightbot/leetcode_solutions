class Solution:
    def removeVowels(self, s: str) -> str:
        temp =  [char for char in s]
        #print(temp)
        #print(temp)
        ans = ""
        for x in range(len(temp)):
            if temp[x]!='a' and temp[x]!='e' and temp[x]!='i' and temp[x]!='o' and temp[x]!='u':
                ans+=str(temp[x])
        return ans
