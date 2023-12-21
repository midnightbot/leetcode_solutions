class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:

        def isChangeNeeded(prev, curr):
            return abs(ord(prev) - ord(curr)) <= 1

        n = len(word)

        @cache
        def find_ans(curr_indx, prev_indx):
            if curr_indx == n:
                return 0

            elif curr_indx == prev_indx:
                return find_ans(curr_indx+1, prev_indx)

            elif curr_indx != prev_indx:
                if isChangeNeeded(word[curr_indx], word[curr_indx-1]):
                    return 1 + min(find_ans(curr_indx+1, curr_indx+1), find_ans(curr_indx+1, curr_indx))
                else:
                    return find_ans(curr_indx+1, prev_indx)
        

        return find_ans(0,0)
