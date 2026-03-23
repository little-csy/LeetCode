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
import threading
import queue
from urllib.parse import urlparse
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        host = urlparse(startUrl).hostname
        q = queue.Queue()
        q.put(startUrl)
        visit = set()
        visit.add(startUrl)
        v_lock = threading.Lock()

        def worker():
            while True:
                url = q.get()
                for nxt in htmlParser.getUrls(url):
                    if urlparse(nxt).hostname == host:
                        with v_lock:
                            if nxt not in visit:
                                visit.add(nxt)
                                q.put(nxt)
                q.task_done()
        
        for _ in range(10):
            t = threading.Thread(target=worker)
            t.daemon = True
            t.start()
        
        q.join()

        return list(visit)
            
        