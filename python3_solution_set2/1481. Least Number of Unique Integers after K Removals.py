class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        ## greedy solution
        ## find freq of all elements and sort the freq
        freq = sorted(list(Counter(arr).values()))
        
        curr = 0
        ## try to remove smaller frequency elements
        ## return the count of remaining numbers
        for indx, x in enumerate(freq):
            if curr + x < k:
                curr += x
            elif curr + x == k:
                return len(freq) - indx - 1
            else:
                return len(freq) - indx
        return 0
