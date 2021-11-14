class Solution:
    def reverseWords(self, s: List[str]) -> None:
        
        strs = []
        
        temp = ""
        for x in range(len(s)):
            if s[x]!=" ":
                temp+=s[x]
                
            else:
                
                strs.append(temp)
                temp = ""
        if temp:
            strs.append(temp)        
        strs = strs[::-1]
        counter = 0
        for x in range(len(strs)):
            for y in range(len(strs[x])):
                s[counter] = strs[x][y]
                counter+=1
                
            if counter < len(s):
                s[counter] = " "
                counter+=1
                
       
        
