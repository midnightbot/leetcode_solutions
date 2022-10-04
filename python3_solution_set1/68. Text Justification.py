##ss
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        thisline = 0
        ans = []
        newword = []
        wordlen = 0
        for x in range(len(words)):
            #print(newword,thisline,wordlen)
            if thisline + len(words[x]) == maxWidth:
                thisline+=len(words[x])
                newword.append(words[x])
                wordlen+=len(words[x])
                
            elif thisline + len(words[x])+1 <= maxWidth:
                thisline+=len(words[x])+1
                newword.append(words[x])
                wordlen+=len(words[x])
                
            elif thisline + len(words[x]) > maxWidth:
                spaces = maxWidth-wordlen
                if len(newword) > 2:
                    gaps = spaces // (len(newword)-1)
                    rem = spaces % (len(newword) - 1)
                    res = ""
                    for y in range(len(newword)):
                        res+=newword[y]
                        for z in range(gaps):
                            res+=" "

                        if y < rem:
                            res+=" "

                    ans.append(res[0:maxWidth])
                    
                elif len(newword)==1:
                    space = maxWidth - len(newword[0])
                    res = ""
                    res+=newword[0]
                    for m in range(space):
                        res+=" "
                    ans.append(res)
                    
                    
                elif len(newword)==2:
                    space = maxWidth - len(newword[0]) - len(newword[1])
                    res = ""
                    res+=newword[0]
                    for m in range(space):
                        res+=" "
                    res+=newword[1]
                    ans.append(res)
                    
                if len(words[x]) == maxWidth:
                    thisline = maxWidth
                    newword = [words[x]]
                    wordlen = maxWidth
                    
                else:
                    thisline =len(words[x])+1
                    newword = [words[x]]
                    wordlen = len(words[x])
                    
        #print(ans)
        ##last line left just
        res = ""
        for x in range(len(newword)):
            res+=newword[x]
            res+=" "
        res = res[0:len(res)-1]
        temp = len(res)
        for m in range(maxWidth - temp):
            res+=" "
            
        ans.append(res)
        
        return ans
                
                    
                
                
                
        
        
