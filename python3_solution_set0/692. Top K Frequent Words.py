class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        ans = []
        words = sorted(words)
        
        print(words)
        visited = []
        for x in range(len(words)):
            if words[x] not in visited:
                visited.append(words[x])
                count = words.count(words[x])
                ans.append((words[x],count))
        
        #print(ans)
        ans = sorted(ans,reverse=True,key = lambda x: (x[1]))
        
        finals = []
        print(ans)
        for y in range(k):
            finals.append(ans[y][0])
        return finals
        
        
            
        
