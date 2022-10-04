##ss
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        
        @lru_cache(None)
        def find_winner(mouse_pos,cat_pos,d):
            
            if d > len(graph) * 3: ## bit risky
                ## else you can try to do it via graph rather than game theory
                return 0
            
            if mouse_pos == cat_pos:
                return 2
            
            if mouse_pos == 0:
                return 1
            
            
            
            if d%2==0:##mouse player
                draw = False
                
                for nei in graph[mouse_pos]:
                    temp = find_winner(nei,cat_pos,d+1)
                    if temp == 1:
                        return 1
                    
                    if temp == 0:
                        draw = True
                        
                if draw:
                    return 0
                else:
                    return 2
                    
                    
            
            if d%2!=0:
                draw = False
                
                for nei in graph[cat_pos]:
                    if nei!=0:
                        temp = find_winner(mouse_pos,nei,d+1)
                        
                        if temp == 2:
                            return 2
                        if temp == 0:
                            draw = True
                            
                if draw:
                    return 0
                else:
                    return 1
                
        return find_winner(1,2,0)
