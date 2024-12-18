Feature: Przetwarzanie zamówień w systemie

  Scenario: Poprawne przetworzenie zamówienia
    Given system jest gotowy do obsługi zamówień
    When tworzę zamówienie na produkt "Laptop" o ilości 2
    And płatność zostaje przetworzona
    Then zamówienie powinno zostać zapisane w bazie danych
