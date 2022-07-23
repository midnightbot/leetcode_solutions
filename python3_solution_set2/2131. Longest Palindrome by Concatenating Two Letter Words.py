##ss
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        same = 0
        diff = 0
        temp = Counter(words)
        
        for x in temp:
            if x[0] == x[1]:
                diff+=temp[x]//2
                same = max(same, 1 if temp[x]%2!=0 else 0)
                
            else:
                c = x[1] + x[0]
                if c in temp:
                    diff+=min(temp[x],temp[c])
                    temp[x] = 0
                    temp[c] = 0
                    
        return diff*4 + same*2
        
