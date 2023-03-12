class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i = 0
        j = 0
        n = len(word)
        comp = []
        num = ''
        for x in abbr:
            if x in '1234567890':
                num+=x

            else:
                if num!='':
                    comp.append(num)
                    num = ''
                comp.append(x)
        if num!='':
            comp.append(num)

        for x in range(len(comp)):
            if comp[x][0] == '0':
                return False
            elif comp[x][0] in '123456789':
                comp[x] = int(comp[x])


        while i < n and j < len(comp):
            if type(comp[j]) == type(1):
                numbr = comp[j]
                i+=numbr
                j+=1

            else:
                if comp[j] == word[i]:
                    i+=1
                    j+=1
                else:
                    return False

        #print(i,j, len(word), comp)
        return i==n and j==len(comp)
