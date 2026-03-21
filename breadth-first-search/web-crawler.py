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
from collections import deque
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        host = startUrl.split("/")[2]
        q = deque()
        q.append(startUrl)
        visit = set()
        visit.add(startUrl)

        while q:
            url = q.popleft()
            for nei in htmlParser.getUrls(url):
                if nei not in visit and nei.split("/")[2] == host:
                    q.append(nei)
                    visit.add(nei)
        
        return list(visit)

        