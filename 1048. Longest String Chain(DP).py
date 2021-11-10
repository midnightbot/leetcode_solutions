class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        words = sorted(words,key=len)
        #print(words)
        
        dp = [-1]*len(words)
        maxs = -float('inf')
        for x in range(len(words)):
            if len(words[x]) > maxs:
                maxs = len(words[x])
        
        counts = 0
        for x in range(len(words)-1,-1,-1):
            if len(words[x]) == maxs:
                counts+=1
                dp[x] = 1
                
            else:
                break
                
        #print(dp)
        
        for x in range(len(words)-1-(counts-1),-1,-1):##for dp array
            if dp[x]!=1:
                temp = 1
                for y in range(x+1,len(words)):##all elemen after x
                    #temp = -float('inf')
                    if len(words[y]) - len(words[x]) == 1:
                        for k in range(len(words[y])):
                            if words[y][k] not in words[x]:
                                #print(words[y][k],words[x],words[y])
                                tss = words[y]
                                #print(tss)
                                tss = tss.replace(words[y][k],"")
                                #print(tss)
                                if words[x] == tss:
                                    #print("hi")
                                    new_dp = 1 + dp[y]
                                    temp = max(temp,new_dp,1)
                                    
                            elif words[y].count(words[y][k]) > words[x].count(words[y][k]):
                                check = []
                                for m in range(len(words[y])):
                                    if words[y][m] == words[y][k]:
                                        check.append(words[y][0:m]+words[y][m+1:len(words[y])])
                                        
                                if words[x] in check:
                                    new_dp = 1 + dp[y]
                                    temp = max(temp,new_dp,1)
                                    
                    
                        
                        dp[x] = temp
        print(dp)
        #print(words)
        return max(dp)
        
