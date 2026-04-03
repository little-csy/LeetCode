class Codec:
    def __init__(self):
        self.id = 0
        self.id2url = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.id += 1
        self.id2url[self.id] = longUrl
        return self.base + str(self.id)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        id = int(shortUrl.split("/")[-1])
        return self.id2url[id]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))