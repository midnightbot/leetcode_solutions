# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ## create a graph from tree
        ## then apply bfs
        ## return node with dist k

        graph = defaultdict(list)
        q = [root]

        while q:
            node = q.pop()

            if node.left:
                graph[node.val].append(node.left.val)
                q.append(node.left)
                graph[node.left.val].append(node.val)
                
            if node.right:
                graph[node.val].append(node.right.val)
                q.append(node.right)
                graph[node.right.val].append(node.val)

        ## now apply bfs on target and return nodes at kth level
        ans = []
        seen = set()
        
        lvl = [[target.val,0]]
        
        while lvl:
            new_lvl = []
            if lvl[0][1] == k:
                return [x[0] for x in lvl]

            for node, dist in lvl:
                seen.add(node)
                for nei in graph[node]:
                    if nei not in seen:
                        new_lvl.append([nei, dist+1])
                        seen.add(nei)

            lvl = new_lvl
            #print(lvl)
            #c+=1
        return []
