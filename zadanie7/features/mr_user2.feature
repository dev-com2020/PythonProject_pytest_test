Feature: Logowanie użytkownika

  Scenario: Użytkownik próbuje się zalogować
    Given użytkownik jest na stronie logowania
    When użytkownik wpisuje poprawny login i hasło
    Then użytkownik zostaje zalogowany
    But użytkownik widzi powiadomienie o nowej wiadomości
