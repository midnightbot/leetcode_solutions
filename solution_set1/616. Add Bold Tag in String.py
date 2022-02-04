##ss
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        
        bold = []
        word = set(words)
        for x in range(len(s)):
            for y in range(x,len(s)+1):
                #print(s[x:y])
                if s[x:y] in word:
                    bold.append((x,y))
         
        if len(bold) >= 1:
            final_bold = []
            prev = bold[0][1]
            start = bold[0][0]
            for x in range(1,len(bold)):
                if bold[x][0] <= prev:
                    prev = max(prev,bold[x][1])

                else:
                    final_bold.append([start,prev])
                    start = bold[x][0]
                    prev = bold[x][1]

            final_bold.append([start,prev])
            #print(final_bold)
            ans = ""
            prev_pointer = 0
            for x in range(len(final_bold)):
                ans+=s[prev_pointer:final_bold[x][0]]
                ans+='<b>'
                ans+=s[final_bold[x][0]:final_bold[x][1]]
                ans+='</b>'
                prev_pointer = final_bold[x][1]

            ans+=s[prev_pointer:]
        
            return ans
        
        else:
            return s
        
    
                
        
