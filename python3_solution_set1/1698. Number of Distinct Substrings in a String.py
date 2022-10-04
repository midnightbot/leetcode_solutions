class TrieNode:
    def __init__(self):
        self.children = {}
class Solution:
    def countDistinct(self, s: str) -> int:
        
        ans=0
        self.ptr = TrieNode()
        for x in range(len(s)):
            start = self.ptr
            for y in range(x,len(s)):
                if s[y] not in start.children:
                    start.children[s[y]] = TrieNode()
                    ans+=1
                    
                start = start.children[s[y]]
                
        return ans
        
