Feature: Obsługa błędów logowania

  Scenario: Użytkownik wpisuje błędne dane logowania
    Given użytkownik jest na stronie logowania
    When użytkownik wpisuje błędne dane logowania
    Then użytkownik widzi komunikat "Niepoprawny login lub hasło"
    Then konto użytkownika pozostaje niezalogowane
