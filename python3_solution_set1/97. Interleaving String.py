##ss
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        ## s1 -> i
        ## s2 -> j
        ## s3 -> indx
        
        @lru_cache(None)
        def find_ans(i,j,indx):
            if indx == len(s3) and i == len(s1) and j == len(s2):
                return True
            elif indx == len(s3):
                return False
            
            elif i < len(s1) and j < len(s2) and s3[indx]!=s1[i] and s3[indx]!=s2[j]:
                return False
            
            else:
                ans = False
                if i < len(s1) and s1[i] == s3[indx]:
                    ans = ans or find_ans(i+1,j,indx+1)
                    
                if j < len(s2) and s2[j] == s3[indx]:
                    ans = ans or find_ans(i,j+1,indx+1)
                    
                return ans
            
        return find_ans(0,0,0)
        
