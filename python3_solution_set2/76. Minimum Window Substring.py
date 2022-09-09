##ss
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""
        
        def make_map(strs):
            res = {}
            
            for x in t:
                if x in res:
                    res[x]+=1
                else:
                    res[x] = 1 
            return res
        
        def checker(maps):
            for x in maps:
                if maps[x] > 0:
                    return False
                
            return True
        
        ans = 10**6
        l = 0
        maps = make_map(t)
        result = ""
        
        for x in range(len(s)):
            
            if s[x] not in maps:
                continue
            
            else:
                maps[s[x]]-=1
                if checker(maps):
                    ### update l
                    #ans = min(ans, x-l+1)
                    it = l
                    done = True
                    while done:
                        if s[it] in maps and maps[s[it]] < 0:
                            maps[s[it]]+=1
                            it+=1
                            
                        elif s[it] in maps and maps[s[it]] == 0:
                            l = it
                            if (x-l+1) < ans:
                                ans = min(ans, x - l + 1)
                                done = False
                                result = s[l:x+1]
                            break
                        
                        else:
                            it+=1
                            
                    ###
                    
        if (x-l+1) < ans and checker(maps):
            #print("hi")
            ans = min(ans, x-l+1)
            result = s[l:x+1]
        
        return result
        
