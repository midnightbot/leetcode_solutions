##ss
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        
        #s = s.split("(")
        know = {}
        for x in range(len(knowledge)):
            know[knowledge[x][0]] = knowledge[x][1]
        #print(ord("("))
        #print(ord(")"))
        transformation1 = {40:'.', 41:',.'}
        
        s = s.translate(transformation1)
        #print(s)
        s = s.split(".")
        #print(s)
        #print(s)
        ans = ""
        for x in range(len(s)):
            #print(s[x][0:len(s[x])-1],s[x][0:len(s[x])-1] in know)
            if len(s[x])>=1 and s[x][-1]==',' and s[x][0:len(s[x])-1] in know:
                ans+=know[s[x][0:len(s[x])-1]]
                
            elif len(s[x])>=1 and s[x][-1]==',' and s[x][0:len(s[x])-1] not in know:
                ans+="?"
                
            elif len(s[x])>=1:
                ans+=s[x]
                
        return ans
        
