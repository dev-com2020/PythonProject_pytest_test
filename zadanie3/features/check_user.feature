Feature: Sprawdzanie dostępności użytkownika

  @system
  Scenario: Użytkownik istnieje w systemie
    Given aplikacja łączy się z API użytkowników
    When sprawdzam użytkownika "john_doe"
    Then odpowiedź powinna zawierać "User exists"
