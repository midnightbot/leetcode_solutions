##ss
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        comp = title.split(" ")
        ans = ""
        
        for x in range(len(comp)):
            if len(comp[x]) <=2:
                ans+=comp[x].lower()
                ans+=" "
            else:
                temp = comp[x].lower()
                ans+=chr(ord(temp[0])-32) + temp[1:]
                ans+=" "
        return ans[:len(ans)-1]
                
        
