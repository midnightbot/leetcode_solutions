class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        ## simple bfs
        ## create graph
        ## digits and its neighbour digits (x+k, x-k)
        graph = {x:[] for x in range(10)}
        
        for x in range(10):
            if x+k < 10:
                graph[x].append(x+k)
            if x-k >= 0:
                graph[x].append(x-k)
                
        ans = set()
        
        ## simple recursion to form the arr
        def find_ans(arr, pos):
            if pos == len(arr): ## one ans found add it in the set
                ans.add(int("".join([str(x) for x in arr])))
            else:
                if len(graph[arr[pos-1]])!=0:
                    for nei in graph[arr[pos-1]]:
                        arr[pos] = nei
                        find_ans(arr, pos+1)
                        
            
        for x in range(1,10):## first digit cannot be 0
            temp = [-1 for x in range(n)]
            temp[0] = x
            find_ans(temp, 1)
        return ans
