import re

class HttpAgent:
    def __init__(self):
        self.data = {}


    def extract_user_data(self, http_response):
        pattern = re.compile(r'Imię: (.*?)\s+Nazwisko: (.*?)$')
        match = pattern.search(http_response)
        if match:
            self.data['first_name'] = match.group(1)
            self.data['last_name'] = match.group(2)
            return True
        return False
