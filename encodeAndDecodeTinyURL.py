class Codec:
    
    def __init__(self):
        self.url_dict = {}
        self.string_length = 6
        self.letters = ("abcdefghijklmnopqrstuvwxyzABCDEF"
                        "GHIJKLMNOPQRSTUVWXYZ0123456789")

    def generate_short_url(self):
        short_url = ""
        for i in range(self.string_length):
            short_url += random.choice(self.letters)
        
        while short_url in self.url_dict:
            short_url = self.generate_short_url()
        return short_url

    def encode(self, longUrl: str) -> str:
        short_url = self.generate_short_url()
        self.url_dict[short_url] = longUrl
        return short_url

    def decode(self, shortUrl: str) -> str:
        if shortUrl in self.url_dict:
            return self.url_dict[shortUrl]
        return None