##ss
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig = []
        let = []
        
        for x in logs:
            if ord('0') <= ord(x[-1]) <= ord('9'):
                dig.append(x)
                
            else:
                let.append(x)
                
        let = [x.split(" ") for x in let]
        let = sorted(let, key = lambda x:(x[1:],x[0]))
        
        let = [" ".join(x) for x in let]
        return let + dig
