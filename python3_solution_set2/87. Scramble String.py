class Solution:
    def isScramble(self, str1: str, str2: str) -> bool:
        
        @cache
        def find_ans(s1, s2):
            m = len(s1)
            n = len(s2)
            if m!=n or sorted(s1)!=sorted(s2):
                return False
            
            elif s1 == s2 or n <= 3:
                return True

            else:
                for x in range(1,m):
                    if (find_ans(s1[:x],s2[:x]) and find_ans(s1[x:], s2[x:])) or (find_ans(s1[:x],s2[-x:]) and find_ans(s1[x:], s2[:-x])):
                        return True
                    
                return False

        return find_ans(str1,str2)
        
