import math
class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        
        jobs = sorted(jobs)
        workers = sorted(workers)
        
        return max([math.ceil(jobs[x]/workers[x]) for x in range(len(jobs))])
        
        
        
