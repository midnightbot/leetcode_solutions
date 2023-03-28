class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:

        ## simple iteration think it like a stack
        ## just check for invalid sequence
        ## whenver we find a chracater increase it count by 1 and reduce the prev character count in 'croak' by -1
        ## this will help maintian the order of elements seen
        
        def check_valid(croakOfFrogs):
            counter = {}

            for x in croakOfFrogs:
                counter[x] = counter.get(x,0) + 1

            return counter['c'] == counter['r'] == counter['o'] == counter['a'] == counter['k']

        '''
        res = 0
        ans = 0

        for x in croakOfFrogs:
            ans = max(ans, res)
            if x == 'c':
                res+=1
            if x == 'k':
                res-=1

        
        return ans if check_valid(croakOfFrogs) else -1
        '''
        def find_sum(arr):
            return sum(list(arr.values())) 
        ans = 0

        arr = {x:0 for x in 'croak'}
        prevs = {'r':'c', 'o':'r', 'a':'o', 'k':'a'}

        for x in croakOfFrogs:
            if x == 'c':
                arr['c']+=1

            elif arr[prevs[x]] == 0:
                return -1

            else:
                if x!='k':
                    arr[x]+=1
                arr[prevs[x]]-=1

            ans = max(ans, find_sum(arr))

        return ans if check_valid(croakOfFrogs) else -1



