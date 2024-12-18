Feature: Pobieranie Flapów
  Scenario: Pobranie istniejącego Flapa
    Given istnieje Flap o identyfikatorze 1
    When użytkownik wysyła zapytanie o ten Flap
    Then powinien otrzymać Flap o nazwie "Przykładowy Flap"
