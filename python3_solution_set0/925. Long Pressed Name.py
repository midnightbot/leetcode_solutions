##ss
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        comp1 = self.find_map(name)
        comp2 = self.find_map(typed)
        
        if len(comp1)!=len(comp2):
            return False
        
        for x in range(len(comp1)):
            if comp1[x][1] != comp2[x][1] or comp1[x][0] > comp2[x][0]:
                return False
            
        return True
        
        
        
    def find_map(self,name):
        comp1 = []
        temp = 1
        for x in range(1,len(name)):
            if name[x] == name[x-1]:
                temp+=1
                
            else:
                comp1.append((temp,name[x-1]))
                temp = 1
                
        comp1.append((temp,name[len(name)-1]))
        print(comp1)
        
        return comp1
        
