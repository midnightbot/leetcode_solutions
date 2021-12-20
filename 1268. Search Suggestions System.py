##ss
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products = sorted(products)
        
        dicts = {}
        
        for x in range(len(products)):
            if products[x][0] in dicts.keys():
                dicts[products[x][0]].append(products[x])
                
            else:
                dicts[products[x][0]] = [products[x]]
                
        ans = []
        temp = ""
        for x in range(len(searchWord)):
            temp+=searchWord[x]
            this = []
            if temp[0] in dicts.keys():
                
                for y in (dicts[temp[0]]):
                    if temp == y[0:len(temp)] and len(this) < 3:
                        this.append(y)
                        
                    elif len(this) == 3:
                        break
                #print(len(this),this)        
                        
            ans.append(this)
                
        return ans
                        
        
