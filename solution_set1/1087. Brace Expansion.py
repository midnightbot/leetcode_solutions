##ss
class Solution:
    def expand(self, s: str) -> List[str]:
        
        result = []
        
        options = {}
        temp = []
        start = False
        thisopt = []
        for x in range(len(s)):
            if s[x]!='}' and s[x]!="{" and start == False:
                temp.append(s[x])
                
            elif s[x] == "{":
                start = True
                
            elif s[x]!="}" and s[x]!="{" and start == True and s[x]!=",":
                thisopt.append(s[x])
                
            elif s[x] == "}":
                start = False
                temp.append("_")
                options[len(temp)-1] = thisopt
                thisopt = []
                
        #print(options,temp)
        
        q = [temp]
        #print(options)
        pointer = 0
        remove = []
        while pointer < len(temp):
            #print(q,pointer)
            for x in range(len(q)):
                if q[x][pointer] == '_':
                    #print("inside",q[x])
                    this = q[x]
                    remove.append(q[x])
                    for z in options[pointer]:
                        new = copy.deepcopy(this)
                        new[pointer] = z
                        q.append(new)
                    
                   
            #print(q,"pre",remove)           
            for y in remove:
                q.remove(y)
                
            remove = []
            pointer+=1
                
        
        #print(q)
        for x in range(len(q)):
            result.append("".join(q[x]))
            
        result = sorted(result)
        return result
        #print(q)

                    
                
        
                
            
        
