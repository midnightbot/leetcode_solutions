##ss
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        stack = []
        
        
        def anangram(str1,str2):
            
            return Counter(str1) == Counter(str2)
        
        
        
        for x in range(len(words)):
            
            if not stack:
                stack.append(words[x])
                
            if not anangram(stack[-1],words[x]):
                stack.append(words[x])
                
        return stack
        
