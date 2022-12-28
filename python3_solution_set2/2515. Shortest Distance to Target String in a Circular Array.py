class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:

        words = words + words + words

        start = len(words)//3 + startIndex
        
        ## move in left and right direction to find the target words

        ans = float('inf')

        for x in range(start, len(words), +1):
            if words[x] == target:
                ans = min(ans, x-start)

        for x in range(start,0,-1):
            if words[x] == target:
                ans = min(ans, start-x)

        return ans if ans!=float('inf') else -1
