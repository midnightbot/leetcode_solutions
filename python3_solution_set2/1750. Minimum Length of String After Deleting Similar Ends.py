class Solution:
    def minimumLength(self, s: str) -> int:
        ## simple two pointer, whenever first and last character match, remove all ooccurences
        ## of that character from both ends
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                temp = s[i]
                while i < len(s) and s[i] == temp:
                    i+=1
                while j > 0 and s[j] == temp:
                    j-=1

            else:
                return j - i + 1

        return max(j - i + 1,0)
        
