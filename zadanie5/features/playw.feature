Feature: Test strony sklepu
  @search
  Scenario: Wyszukiwanie w sklepie
    Given ładujemy adres strony
    When Szukam "shirt"
    And długość tytułu musi wynosić 15 znaków
    Then Powinna wyświetlić się strona z koszulkami


  @title @ignore
  Scenario: Sprawdzenie tytułu strony
    Given ładujemy adres strony
    Then strona powinna wyświetlić "Home Page"

