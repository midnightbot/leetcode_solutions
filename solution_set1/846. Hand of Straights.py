##ss
##simple dict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        hand = sorted(hand)
        dicts = {}
        keys = 0
        for x in range(len(hand)):
            if hand[x] in dicts:
                dicts[hand[x]]+=1
                
            else:
                keys+=1
                dicts[hand[x]] = 1
                
        while dicts:
            count = 0
            #print(dicts)
            done = False
            if keys < groupSize:
                return False
            for x in dicts:
                if count == groupSize:
                    done = True
                    break
                if count == 0:
                    prev = x
                    
                else:
                    if x!=prev+1:
                        return False
                    
                    prev = x
                    
                count+=1
                
            if count == groupSize:
                done = True
                
            if done == True:
                count = 0
                remove = []
                for x in dicts:
                    if count == groupSize:
                        break
                        
                    dicts[x]-=1
                    if dicts[x] == 0:
                        remove.append(x)
                        
                    count+=1
                for x in range(len(remove)):
                    keys-=1
                    dicts.pop(remove[x])
                    
        return True
                    
                
                    
                
                
                
        
