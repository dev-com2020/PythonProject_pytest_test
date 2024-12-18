from zadanie8.features.steps.commands import UtworzFlapCommand
from zadanie8.features.steps.queries import PobierzFlapQuery


class FlapCommandHandler:
    def __init__(self):
        self.wykonane_polecenia = []

    def obsluz(self, polecenie):
        if isinstance(polecenie, UtworzFlapCommand):
            self.wykonane_polecenia.append(polecenie)
            return "Flap został utworzony"


class FlapQueryHandler:
    def obsluz(self, zapytanie):
        if isinstance(zapytanie, PobierzFlapQuery):
            # Stub zwraca wstępnie zdefiniowane dane
            return {"id": zapytanie.flap_id, "nazwa": "Przykładowy Flap"}
