class Solution:
    def numDifferentIntegers(self, word: str) -> int:

        strs = ""
        temp = set()
        for x in word:
            if x in "1234567890":
                strs+=x
            else:
                strs+=" "

        t = strs.split(" ")
        #print(t)
        t = [int(x) if x!=""  else -1 for x in t]
        temp = set(t)
        if -1 in temp:
            return len(temp) - 1
        else:
            return len(temp)
