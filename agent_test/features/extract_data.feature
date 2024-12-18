Feature: Wyodrębnianie danych z protokołu HTTP

  Scenario: Poprawne wyodrębnienie danych z odpowiedzi HTTP
    Given Uruchomiono agenta HTTP
    When Otrzymuje odpowiedź HTTP z danymi użytkownika
    Then Agent powinien wyodrębnić imię "Jan" i nazwisko "Kowalski"