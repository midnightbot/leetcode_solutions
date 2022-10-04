##ss
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        ##if s1[i] == s2[j] -> i+=1 j+=1
        
        ##else min(ascii(s1[i]) + solve(i+1,j), ascii(s2[j]) + solve(i,j+1))
        
        @lru_cache(None)
        def match(i,j):
            #print(i,j)
            if i >= len(s1) or j >= len(s2):
                c = 0
                for z in range(i,len(s1)):
                    c+=ord(s1[z])
                    
                #print(c,"old")
                for z in range(j, len(s2)):
                    c+=ord(s2[z])
                    
                #print(c,"new")
                return c
            
            elif i < len(s1) and j < len(s2):
                if s1[i]!=s2[j]:
                    part1 = ord(s1[i]) + match(i+1,j)
                    part2 = ord(s2[j]) + match(i,j+1)

                    return min(part1, part2)
                
                else:
                    return match(i+1,j+1)
        
        return match(0,0)
