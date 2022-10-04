##ss
class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        textsize = 0
        words = []
        cons = 0
        thisword = ""
        for x in range(len(text)):
            if text[x]==" ":
                if cons!=0:
                    #words+=1
                    cons = 0
                    words.append(thisword)
                    thisword = ""
                #textsize+=1
            else:
                cons+=1
                textsize+=1
                thisword+=text[x]
        if cons!=0:
            words.append(thisword)
        spaces = len(text) - textsize
        ##now we need number of words
        ##extra spaces
        if spaces == 0:
            return text
        
        if len(words) == 1:
            ans = words[0] + ''.join([" " for x in range(len(text)-textsize)])
            return ans
        equ = spaces // (len(words)-1)
        extra = spaces % (len(words)-1)
        
        ans = ""
        for x in range(len(words)):
            ans+=words[x]
            for z in range(equ):
                ans+=" "
                
        ans = ans[:-1*equ]
        for x in range(extra):
            ans+=" "
        return ans
        
