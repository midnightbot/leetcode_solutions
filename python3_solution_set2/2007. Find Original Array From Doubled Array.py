class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ans = []
        changed.sort()
        maps = Counter(changed)
        #print(changed)
        for x in maps:
            if x == 0:
                if (maps[x])%2!=0:
                    return []
                else:
                    for it in range(maps[x]//2):
                        ans.append(0)
                        
                        
            else:
                if 2*x in maps:
                    if maps[2*x] < maps[x]:
                        return []
                    else:
                        maps[2*x]-=maps[x]
                        for it in range(maps[x]):
                            ans.append(x)
                elif maps[x]!=0 and 2*x not in maps:
                    return []
                            
        return ans
