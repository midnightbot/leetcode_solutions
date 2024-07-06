class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:

        n = len(colors)
        colors = colors+[colors[0],colors[1]]

        ans = 0
        for x in range(n):
            if colors[x:x+3] in [[0,1,0], [1,0,1]]:
                ans+=1
        return ans
        
