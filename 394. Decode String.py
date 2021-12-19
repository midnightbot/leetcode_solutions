class Solution:
    def decodeString(self, s: str) -> str:
        
        count = []
        strings = []
        
        ans = ""
        k = 0 
        for x in range(len(s)):
            if s[x].isdigit():
                k = k *10 + ord(s[x]) - ord('0')
                
            elif s[x] == "[":
                count.append(k)
                strings.append(ans)
                ans = ""
                k = 0
                
            elif s[x] == "]":
                new_s = strings.pop()
                new_c = count.pop()
                for m in range(new_c-1,-1,-1):
                    new_s+=ans
                    
                ans = new_s
                
            else:
                ans+=s[x]
                
        return ans
        
