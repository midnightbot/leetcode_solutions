##ss
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        
        
        ## simple recursion
        ##add spaces in s, where number of spaces = len(pattern) - 1
        ##and then check if any one of the combination forms a bijective mapping
        
        breaks = []
        
        def expand(s,pointer,words,prev_str,ans):
            #print(s,pointer,prev_str,ans)
            if pointer == len(s) and words == 1:
                
                ans.append(prev_str)
                #print(ans)
                breaks.append(ans)
                
            elif pointer < len(s) and words > 0:
                new_str = prev_str + s[pointer]
                
                expand(s,pointer+1,words,new_str,ans)
                
                newans = copy.copy(ans)
                newans.append(prev_str)
                n_str = s[pointer]
                
                expand(s,pointer+1,words-1,n_str,newans)
                
                
        expand(s,1,len(pattern),s[0],[])
        #print(breaks)
        for x in range(len(breaks)):
            dicts = {}
            count = 0
            used = set()
            for y in range(len(breaks[x])):
                keys = pattern[y]
                
                vals = breaks[x][y]
                
                if keys not in dicts and vals not in used:
                    count+=1
                    dicts[keys] = vals
                    used.add(vals)
                    
                elif keys in dicts and dicts[keys]!=vals:
                    break
                    
                elif keys in dicts and dicts[keys] == vals:
                    count+=1
                    
                    
            if count == len(pattern):
                return True
            
            
        return False
                    
                
            
            
