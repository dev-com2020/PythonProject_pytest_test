from zadanie8.features.steps.commands import UtworzFlapCommand
from zadanie8.features.steps.handlers import FlapCommandHandler, FlapQueryHandler
from zadanie8.features.steps.queries import PobierzFlapQuery


def test_utworz_flap():
    handler_polecen = FlapCommandHandler()
    polecenie = UtworzFlapCommand("Testowy Flap")

    wynik = handler_polecen.obsluz(polecenie)

    assert wynik == "Flap został utworzony"
    assert polecenie in handler_polecen.wykonane_polecenia


def test_pobierz_flap():
    handler_zapytania = FlapQueryHandler()
    zapytanie = PobierzFlapQuery(1)

    wynik = handler_zapytania.obsluz(zapytanie)

    assert wynik == {"id": 1, "nazwa": "Przykładowy Flap"}
