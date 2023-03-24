class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        ## pattern is list of three websites

        g = {}
        all_patterns = set()
        user_patterns = {}
        cnt = {}
        
        ## find how many users have this pattern
        def find_cnt(p):
            c = 0
            for it in user_patterns:
                if p in user_patterns[it]:
                    c+=1

            return c
        
        ## store all patterns for all users
        def generate_user_pattern(user_name, site_list):
            seen = set()
            if len(site_list) < 3:
                user_patterns[user_name] = seen
            else:
                n = len(site_list)
                for x in range(n-2):
                    for y in range(x+1,n-1):
                        for z in range(y+1,n):
                            seen.add((site_list[x], site_list[y], site_list[z]))

                user_patterns[user_name] = seen
        
        ## sort the username, timestamp, website array with increasing timestamp value
        indx = [(timestamp[x],x) for x in range(len(timestamp))]
        indx = sorted(indx, key = lambda x:x[0])
        indx = [x[1] for x in indx]
        timestamp1 = [timestamp[x] for x in indx]
        username1 = [username[x] for x in indx]
        website1 = [website[x] for x in indx]

        for x,y,z in zip(username1, timestamp1, website1):
            if x in g:
                g[x].append(z)
            else:
                g[x] = [z]

        ## create pattern for all users 
        ## also maintain all unique patterns seen till now
        for it in g:
            generate_user_pattern(it, g[it])
            all_patterns |= user_patterns[it]

        ## find count of each pattern
        for it in all_patterns:
            cnt[it] = find_cnt(it)

        cnt = [[cnt[it], it] for it in cnt]

        ## sort it based on count and for tiebreaker use lexical sort
        ## for lexicographically sort first sort by len then by value
        cnt = sorted(cnt, key = lambda x:(-x[0], len(x[1]),x[1]))
        
        return cnt[0][1]
