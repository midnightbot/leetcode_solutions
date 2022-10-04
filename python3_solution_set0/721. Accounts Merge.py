class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        graph = defaultdict(set) ## simple dictionary but avoiding duplicates
        
        emailtoName = {} ## to map each email to its owner name
        
        for acc in accounts:
            name = acc[0]
            email1 = acc[1]
            emailtoName[email1] = name
            
            for emails in acc[2:]: ##connecting all emails of same owner
                graph[email1].add(emails)
                graph[emails].add(email1)
                emailtoName[emails]  = name
                
        ans  = []
        seen = set()
        
        
        for email in emailtoName:
            if email not in seen:
                stack = [email]
                seen.add(email)
                emails = []
                
                while stack:##find all emails that are linked to this current email
                    cur = stack.pop()
                    emails.append(cur)
                    
                    for nei in graph[cur]:
                        if nei not in seen:
                            stack.append(nei)
                            seen.add(nei)
                            
                ans.append([emailtoName[email]] + sorted(emails))
                
                
        return ans
        
