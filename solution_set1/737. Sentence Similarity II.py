##ss
class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        ##a-b, b-c then a-c
        ##simple union find
        sims = {}
        allwords = set()
        if len(sentence1)!= len(sentence2):
            return False
        
        parent = {}
        
        def find_parent(p):
            #print(p)
            if p not in parent:
                #parent[p] = p
                return p
            parent[p] = find_parent(parent[p])
            return parent[p]
        
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                parent[xs] = ys
                
            
        for x in range(len(similarPairs)):
            allwords.add(similarPairs[x][0])
            allwords.add(similarPairs[x][1])
            if find_parent(similarPairs[x][0])!= find_parent(similarPairs[x][1]):
                union(similarPairs[x][0],similarPairs[x][1])
                
        #print(parent)
        for x in parent:##one more iteration is required to group all transitive words into single groups
            find_parent(x)
        
        for x in allwords:
            if x not in parent:
                parent[x] = x
        #print("done") 
        #print(parent)
        for x in range(len(sentence1)):
            if sentence1[x] == sentence2[x] or (sentence1[x] in parent and sentence2[x] in parent and parent[sentence1[x]]== parent[sentence2[x]]):
                #print(x)
                continue
            else:
                return False
            
        return True
        #print(parent)
