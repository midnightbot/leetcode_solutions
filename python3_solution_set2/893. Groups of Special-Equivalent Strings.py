class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:

        ## make the smallest word that can be made after moves on a string

        def make_word(s):
            e = []
            o = []
            for x in range(len(s)):
                if x%2==0:
                    e.append(s[x])
                else:
                    o.append(s[x])

            e.sort()
            o.sort()
            return ''.join(e) + ''.join(o)

        counter = set()
        maxs = 0
        for it in words:
            new_word = make_word(it)
            counter.add(new_word)
            #counter[new_word] = counter.get(new_word,0)+1
            #maxs = max(maxs, counter[new_word])
        return len(counter)
