##ss
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        
        parent = {}
        
        def find_parent(x):
            if x not in parent:
                return x
            parent[x] = find_parent(parent[x])
            
            return parent[x]
        
        
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                parent[xs] = ys
                return True
            
            return False
        
        
        for a,b in synonyms:
            union(a,b)
         
        #print(parent)
        for x in parent:
            find_parent(x)
            
        #print(parent)
        grps = {}
        
        for x in parent:
            if parent[x] in grps:
                grps[parent[x]].add(x)
                
            else:
                grps[parent[x]] = {x}
                
        for x in grps:
            grps[x].add(x)
        
        add = {}
        for x in grps:
            for y in grps[x]:
                if y not in grps:
                    add[y] = grps[x]
                    
        for x in add:
            grps[x] = add[x]
        #print(grps)
        result = []
        
        
        def make_ans(pointer, ans, left):
            #print(pointer,ans,left)
           
            if pointer == len(text):
                #print("inside")
                result.append(" ".join(ans))
                
            else:
                for z in left:
                    newans = copy.deepcopy(ans)
                    newans[pointer] = z
                    if pointer + 1 < len(text):
                        #print(text[pointer+1])
                        if text[pointer+1] in grps:
                            options = copy.deepcopy(grps[text[pointer+1]])
                            #print(options, "seeing options")
                            make_ans(pointer+1,newans,options)
                        else:
                            make_ans(pointer+1,newans,{text[pointer+1]})
                            
                    else:
                        make_ans(pointer+1,newans,[])
                
            
        text = text.split(" ")
        thisans = [-1 for x in range(len(text))]
        if text[0] in grps:
            opt = grps[text[0]]
        else:
            opt = {text[0]}
            
        #print(grps)
        make_ans(0,thisans,opt)
        #print(grps)
        #print((result))
        
        return sorted(result)
