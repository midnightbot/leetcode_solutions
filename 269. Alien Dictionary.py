##ss
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        ##simple topological ordering
        ##topological ordering using bfs
        
        dicts = {c:set() for x in words for c in x} ## contains all unique words and their mapping.
        ##basically a graph a->w and so on
        
        #print(dicts.keys())
        
        for x in range(len(words)-1):
            word1 = words[x]
            word2 = words[x+1]
            
            mins = min(len(word1),len(word2))
            if len(word1) > len(word2) and  word1[:mins] == word2[:mins]:##checking the condition that if two strings have same prefix then smaller string should be first in the words or else there will be no answer
                
                return ""
            
            for y in range(mins):##making the graph
                if word1[y]!=word2[y]:
                    dicts[word1[y]].add(word2[y])
                    break
                    
        visited = {}
        ##visited[x] = False indicates it is once visited
        ##visited[x] = True indicates this x is in the current path considered
        temp  = []
        
        def expand(c):
            
            if c in visited: ## if c is already in this path
                return visited[c]
            
            visited[c] = True ##adding this c to current path
            for neigh in dicts[c]:
                if expand(neigh):##if same element again found in same path, there is cycle formed and hence there will be no ordering possible
                    return True
                
                
            visited[c] = False ##this path is fully explored, hence reset c as visited and not seen in the next new path
            
            temp.append(c)
            
        for x in dicts.keys():
            if expand(x):##if cycle is found expand(x) will return true and hence no answer can be found
                return ""
            
        temp = temp[::-1]
        ans = "".join(temp)
        return ans
                
        
