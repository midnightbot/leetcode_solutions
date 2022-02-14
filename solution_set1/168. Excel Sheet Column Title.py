import math
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        ##single = 26  (26)
        ##double chr 26*26 (702)
        ##triple 26*26*26 (18278)
        ##quadraple 26*26*26*26 (475254)
        arr = [0,26, 702, 18278, 475254]
        maps = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
       
        ahead = columnNumber 
        ans = []
        #print(ahead)
        while ahead > 0:
            ans.append(maps[(ahead-1)%26])
            
            ahead = (ahead-1) // 26
            #print(ahead)
        ans = ans[::-1]
        return ''.join(ans)
        
