class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        ans = []
        count = len(s)
        temp = 0
        for x in range(len(words)):
            temp+= len(words[x])
            if temp!=count:
                ans.append(len(words[x]))
                
            elif temp==count:
                break
        print(x)
        compare = ""
        for y in range(x+1):
            compare+=words[y]
            
        if compare==s:
            return True
        else:
            return False
        
