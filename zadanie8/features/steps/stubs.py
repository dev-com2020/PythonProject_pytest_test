from zadanie8.features.steps.queries import PobierzFlapQuery


class StubQueryHandler:
    def handle(self, query):
        if isinstance(query, PobierzFlapQuery) and query.flap_id == 1:
            return {"id": query.flap_id, "nazwa": "Przykładowy Flap"}
        return None
