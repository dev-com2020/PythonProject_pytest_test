class Service:
    def fetch_data(self):
        return "Data"

def process_data(service):
    data = service.fetch_data()
    print(f"Processing {data}")

class MockService:
    def fetch_data(self):
        return "Mock..."

process_data(MockService())