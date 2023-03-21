class Solution:
    def boldWords(self, words: List[str], s: str) -> str:

        tags = []
        words = set(words)
        ## words[i].length == 10
        ## for each index find a start point such that the substring formed is seen in words
        for x in range(len(s)+1):
            for y in range(max(0, x-11),x,1):
                if s[y:x] in words:
                    tags.append([y,x])
                    break

        ## combine the tags to avoid overlaps
        tags.append([float('inf'), float('inf')])
        tags = sorted(tags, key = lambda x:(x[0],-x[1]))
        ans = []
        prev_start = tags[0][0]
        prev_end = tags[0][1]
        #print(tags)
        for x,y in tags:
            if prev_start <= x <= prev_end:
                prev_end = max(prev_end, y)

            else:
                ans.append([prev_start,prev_end])
                prev_start = x
                prev_end = y
        #print(ans)
        ans.append([float('inf'), float('inf')])
        i = 0
        j = 0
        result = ''
        while i < len(s):
            if ans[j][0] == i:
                result+='<b>' + s[ans[j][0]:ans[j][1]] + '</b>'
                i = ans[j][1]
                j+=1
            else:
                result+=s[i]
                i+=1
        return result
