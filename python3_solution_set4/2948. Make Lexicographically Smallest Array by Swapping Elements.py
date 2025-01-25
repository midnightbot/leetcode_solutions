class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums = [[nums[x],x] for x in range(len(nums))]
        nums = sorted(nums, key = lambda x:x[0])

        n = len(nums)

        parent = [x for x in range(len(nums))]

        def find_parent(x):
            if parent[x] == x:
                return x
            parent[x] = find_parent(parent[x])
            return parent[x]

        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            if xs!=ys:
                parent[min(xs,ys)] = max(xs,ys)


        for x in range(1,len(nums)):
            if abs(nums[x][0] - nums[x-1][0]) <= limit:
                union(x,x-1)

        for x in range(len(parent)):
            find_parent(x)

        # now just sort elements in individual grps
        indx_grps = {}
        grps = {}

        for x in range(len(parent)):
            if parent[x] in indx_grps:
                indx_grps[parent[x]].append(nums[x][1])
                grps[parent[x]].append(nums[x][0])
            else:
                indx_grps[parent[x]] = [nums[x][1]]
                grps[parent[x]] = [nums[x][0]]

        # print(indx_grps, grps)
        for x in grps:
            grps[x].sort()
            indx_grps[x].sort()

        ans = [0 for x in range(n)]
        
        for x in grps:
            for y in range(len(indx_grps[x])):
                ans[indx_grps[x][y]] = grps[x][y]

        return ans
        
