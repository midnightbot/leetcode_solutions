##ss
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        
        #ans = set()
        visited = set()
        
        q = [startUrl]
        visited.add(startUrl)
        while q:
            node = q.pop(0)
            t = node.split("//")
            t2 = t[1].split("/")
            t = htmlParser.getUrls(node)
            for y in t:
                temp = y.split("//")
                temp2 = temp[1].split("/")
                
                if y not in visited and temp2[0] == t2[0]:
                    q.append(y)
                    visited.add(y)
                    
        return visited
        
