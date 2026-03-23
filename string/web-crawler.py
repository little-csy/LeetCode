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
        host = startUrl.split('/')[2]
        q = deque()
        visit = set()
        q.append(startUrl)
        visit.add(startUrl)

        while q:
            url = q.popleft()

            for nxt in htmlParser.getUrls(url):
                if nxt.split('/')[2] == host:
                    q.append(nxt)
                    visit.add(nxt)
        
        return list(visit)