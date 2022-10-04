##ss
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        comp = Counter(tasks)
        rounds = 0
        
        for x in comp:
            
            if comp[x]%3 == 0:
                rounds+= comp[x] // 3
                comp[x] = 0
            
            else:
                div = comp[x] // 3
                rems = comp[x] % 3
                
                if rems == 1 and div!=0:
                    rounds+= div - 1
                    rounds+= 2
                    comp[x] = 0
                    
                elif rems == 2:
                    rounds+= div + 1
                    comp[x] = 0
                    
            if comp[x]!=0:
                return -1
            
            
        return rounds
                    
                
