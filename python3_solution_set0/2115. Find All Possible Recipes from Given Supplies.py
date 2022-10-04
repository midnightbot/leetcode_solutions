##ss
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        c = 0
        og_rec = copy.copy(recipes)
        prev_len = -1
        while len(supplies)!=prev_len and len(recipes)!=0:
            prev_len = len(supplies)
            var = False
            
            #print(len(recipes))
            for x in range(len(recipes)):
                if recipes[x]!=-1:
                    var = False
                    temps = []
                    for z in range(len(ingredients[x])):
                        if ingredients[x][z] not in supplies:
                            var = True
                            break
                        else:
                            temps.append(ingredients[x][z])
                            
                            
                    ingredients[x] = list(set(ingredients[x]) - set(temps))
                            
                    if var == False:
                        supplies.append(recipes[x])
                        #temps.append(recipes)
                        recipes.pop(x)  
                        ingredients.pop(x)
                        break
              
            #print(recipes)
            

        ans = []
        #print(recipes)
        return set(og_rec) - set(recipes)
                    
            
        
