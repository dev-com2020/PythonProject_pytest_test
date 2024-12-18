#Specyfikacja:
# System powinien akceptować rezerwację tylko wtedy, gdy pasażer jest pełnoletni
# i wybrał dostępny lot.
Feature: Rezerwacja lotu
  Scenario: Poprawna rezerwacja lotu
    Given Pasażer "Jan Kowalski" ma 30 lat
    And Lot "Warszawa - Londyn" jest dostępny
    When Pasażer rezerwuje lot "Warszawa - Londyn"
    Then Rezerwacja jest potwierdzona

  Scenario: Niepełnoletni pasażer próbuje rezerwować lot
    Given Pasażer "Janek Kowalski" ma 15 lat
    And Lot "Warszawa - Paryż" jest dostępny
    When Pasażer próbuje zarezerwować lot "Warszawa - Paryż"
    Then Rezerwacja jest odrzucona z powodu wieku
