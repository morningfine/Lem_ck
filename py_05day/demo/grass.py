class Grass(object):
    url_map = {}

    def router(self, url):
        def decorator(f):
            self.add_url_to_map(url, f)
            return f

        return decorator

    def add_url_to_map(self, url, f):
        self.url_map[url] = f
