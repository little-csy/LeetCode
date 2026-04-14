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
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = startUrl.split('/')[2]
        q = queue.Queue()
        visit = set()
        q.put(startUrl)
        visit.add(startUrl)
        lock = threading.Lock()
        
        def worker():
            while True:
                node = q.get()
                for nxt in htmlParser.getUrls(node):
                    with lock:
                        if nxt not in visit and nxt.split('/')[2] == hostname:
                            q.put(nxt)
                            visit.add(nxt)
                q.task_done()
        
        for _ in range(4):
            t = threading.Thread(target=worker)
            t.daemon = True
            t.start()
        
        q.join()

        return list(visit)       