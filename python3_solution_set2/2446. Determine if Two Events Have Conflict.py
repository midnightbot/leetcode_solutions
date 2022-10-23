class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        conv = []
        
        def convs(strs):
            temp = strs.split(":")
            return int(temp[0])*60 + int(temp[1])
        
        
        conv.append([convs(event1[0]),+1])
        conv.append([convs(event1[1])+0.01,-1])
        conv.append([convs(event2[0]),+1])
        conv.append([convs(event2[1])+0.01,-1])
        
        conv = sorted(conv, key = lambda x:x[0])
        
        c = 0
        
        for x in conv:
            c+=x[1]
            if c == 2:
                return True
            
        return False
