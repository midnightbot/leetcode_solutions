class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans = []
        maps = {}
        for i,x in enumerate(order):
            maps[x]=i
        
        for i,x in enumerate(friends):
            ans.append([x, maps[x]])

        ans = sorted(ans, key = lambda x:x[1])
        return [x[0] for x in ans]
        
