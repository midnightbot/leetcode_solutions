##ss
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        parent = {}
        
        def find_parent(x):
            if x not in parent:
                return x
            
            parent[x] = find_parent(parent[x])
            return parent[x]
        
        
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                parent[xs] = ys
                
                return True
            
            return False
        
        
        equality = []
        inequality = []
        
        
        
        for x in range(len(equations)):
            if equations[x][1]=='=':
                equality.append(equations[x])
                
            else:
                inequality.append(equations[x])
                
        for x in range(len(equality)):
            union(equality[x][0],equality[x][-1])
          
        #print(parent) 
        for x in range(len(inequality)):
            par1 = find_parent(inequality[x][0])
            par2 = find_parent(inequality[x][-1])
            #print(par1,par2,parent)
            if par1 == par2:
                return False
            
        return True
              
            
        
