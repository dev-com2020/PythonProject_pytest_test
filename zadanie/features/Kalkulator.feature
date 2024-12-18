Feature: Dodawanie licz
  Scenario: Dodawanie dwóch liczb
    Given liczby 2 i 3
    When obliczam sumę
    Then wynik powinien wynosić 5