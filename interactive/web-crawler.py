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
        hostname = startUrl.split('/')[2]
        q = deque()
        visit = set()
        q.append(startUrl)
        visit.add(startUrl)
        while q:
            node = q.popleft()
            for nxt in htmlParser.getUrls(node):
                if nxt.split('/')[2] == hostname and nxt not in visit:
                    q.append(nxt)
                    visit.add(nxt)
        return list(visit)