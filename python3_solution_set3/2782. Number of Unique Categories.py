# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        # union find
        parent = [-1] * n
        
        def find_parent(x):
            if parent[x] == -1:
                return x
            parent[x] = find_parent(parent[x])
            return parent [x]
        
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                parent[ys] = xs

        # print(categoryHandler.haveSameCategory(0,1))
        for x in range(n):
            for y in range(x+1,n):
                if categoryHandler.haveSameCategory(x,y):
                    union(x,y)

        # print(parent)
        return parent.count(-1)
