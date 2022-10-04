##ss
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        mapping = {}
        seen = set()
        curr = 0
        for x in range(len(key)):
            if key[x] not in seen and key[x]!=" ":
                seen.add(key[x])
                mapping[key[x]] = chr(curr + ord('a')) 
                curr+=1
            else:
                continue
                
        mapping[" "] = " "
        #print(mapping)
        return "".join([mapping[x] for x in message])
