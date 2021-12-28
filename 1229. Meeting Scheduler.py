##ss
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        slots1 = sorted(slots1, key = lambda x:x[0])
        slots2 = sorted(slots2, key = lambda x:x[0])
        
        i = 0
        j = 0
        #print(slots1)
        #print(slots2)
        while i < len(slots1) and j < len(slots2):

            starts = max(slots1[i][0],slots2[j][0])
            ends = min(slots1[i][1],slots2[j][1])

            if ends - starts >= duration:
                return [starts,starts+duration]

            elif slots1[i][1] < slots2[j][1]:
                i+=1
                
            else:
                j+=1
        return []
        
