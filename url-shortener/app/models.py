# TODO: Implement your data models here
# Consider what data structures you'll need for:
# - Storing URL mappings
# - Tracking click counts
# - Managing URL metadata

import threading
from datetime import datetime

# This class acts like an in-memory database
class URLStore:
    def __init__(self):
        # Lock to ensure thread-safe access to shared data
        self.lock = threading.Lock()
        # Dictionary to store short_code → metadata
        self.data = {}

    def add_url(self, short_code, original_url):
        # Safely add a new short URL mapping
        with self.lock:
            self.data[short_code] = {
                "url": original_url,                      # original long URL
                "clicks": 0,                               # number of times short URL is used
                "created_at": datetime.utcnow().isoformat() # time when short URL was created
            }

    def get_url(self, short_code):
        # Safely fetch original URL metadata for a short code
        with self.lock:
            return self.data.get(short_code)

    def increment_click(self, short_code):
        # Safely increase click count on redirection
        with self.lock:
            if short_code in self.data:
                self.data[short_code]["clicks"] += 1

    def get_stats(self, short_code):
        # Safely return analytics (clicks, time, url)
        with self.lock:
            return self.data.get(short_code)

# Global store instance
store = URLStore()


