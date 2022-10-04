class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        def lcs(str1,str2):
            dp = [["" for x in range(len(str1)+1)] for y in range(len(str2)+1)]
            
            for x in range(len(str2)):
                for y in range(len(str1)):
                    if str1[y] == str2[x]:
                        dp[x+1][y+1] = dp[x][y] + str2[x]
                        
                    else:
                        dp[x+1][y+1] = max(dp[x+1][y], dp[x][y+1],key=len)
                        
            return dp[-1][-1]
            
        ans = lcs(str1,str2)
        
        result = ""
        i = 0
        j = 0
        
        for x in ans:
            while str1[i]!= x:
                result+=str1[i]
                i+=1
                
            while str2[j]!=x:
                result+=str2[j]
                j+=1
                
            result+=x
            
            i+=1
            j+=1
            
        return result + str2[j:] + str1[i:]
