##ss
class Solution:
    def toHexspeak(self, num: str) -> str:
        
        temp = str(format(int(num), '02x'))
        
        check = [x for x in temp]
        
        for x in range(len(check)):
            if check[x]!='0':
                break
                
        check = check[x:]
        for x in range(len(check)):
            
            if check[x] == '0':
                check[x] = 'O'
                
            elif check[x] == '1':
                check[x] = 'I'
                
            elif check[x] in ['a','b','c','d','e','f','i','o']:
                continue
                
            else:
                return "ERROR"
            
        return "".join(check).upper()
