"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def isleaf(grid):
            b = 0
            w = 0
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if grid[x][y] == 1:
                        b+=1
                    else:
                        w+=1
            return (b==0 or w==0)

        def find_ans(img):
            n = len(img)

            if img is None:
                return None

            if isleaf(img):
                return Node(img[0][0], True, None, None, None, None)
            
            else:
                tl = find_ans([row[:n//2] for row in img[:n//2]])
                tr = find_ans([row[n//2:] for row in img[:n//2]])
                bl = find_ans([row[:n//2] for row in img[n//2:]])
                br = find_ans([row[n//2:] for row in img[n//2:]])
                return Node("*", False,tl,tr,bl,br)

        return find_ans(grid)
        
