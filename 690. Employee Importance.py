"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

##ss
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        ans = 0
        for x in range(len(employees)):
            if employees[x].id == id:
                break
                
        queue = [employees[x].id]    
        while queue:
            node = queue.pop(0)
            #index,ans+=self.find_imp(self,employees,node)
            #index = self.find_imp(self,employees,node[0])[0]
            index = self.find_imp(employees,node)[0]
            ans+=self.find_imp(employees,node)[1]
            
            for x in employees[index].subordinates:
                queue.append(x)
                
        return ans
            
            
            
        
        
        
    def find_imp(self,employees,ids):
        
        for x in range(len(employees)):
            if employees[x].id == ids:
                return x,employees[x].importance
            
            
    #def get_id(self,employees,ids)
        
